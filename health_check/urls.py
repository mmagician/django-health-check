from django.conf.urls import url, patterns

from health_check.views import MainView


urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='health_check_home'),
    url(r'^celery_remote$', MainView.as_view(registry='_registryremote'), name='celery_remote'),
    url(r'^celery_default$', MainView.as_view(registry='_registrydefault'), name='celery_remote'),
)
