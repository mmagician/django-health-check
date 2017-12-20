from django.apps import AppConfig
from django.conf import settings

from health_check.plugins import plugin_dir


class HealthCheckConfig(AppConfig):
    name = 'health_check.contrib.celery'

    def ready(self):
        from .backends import CeleryHealthCheck

        for queue in settings.CELERY_QUEUES:
            celery_class_name = 'CeleryHealthCheck' + queue.title()

            celery_class = type(celery_class_name, (CeleryHealthCheck,), {'queue': queue})
            plugin_dir.register(celery_class)
