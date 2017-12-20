import copy

from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from health_check.plugins import plugin_dir

@csrf_exempt
class MainView(TemplateView):
    template_name = 'health_check/index.html'
    registry = '_registry'

    def get_object(self, queryset=None):
        return queryset.get(registry=self.registry)

    @never_cache
    def get(self, request, *args, **kwargs):
        plugins = []
        errors = []
        for plugin_class, options in getattr(plugin_dir, self.registry):
            plugin = plugin_class(**copy.deepcopy(options))
            plugin.run_check()
            plugins.append(plugin)
            errors += plugin.errors
        plugins.sort(key=lambda x: x.identifier())
        status_code = 500 if errors else 200

        if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            return self.render_to_response_json(plugins, status_code)

        return self.render_to_response({'plugins': plugins}, status=status_code)

    def render_to_response_json(self, plugins, status):
        return JsonResponse(
            {str(p.identifier()): str(p.pretty_status()) for p in plugins},
            status=status
        )
