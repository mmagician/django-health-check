from django.conf.urls import url, patterns

from health_check.views import MainView


urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='health_check_home'),
)
