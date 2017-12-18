from django.apps import AppConfig

from health_check.plugins import plugin_dir
from django.conf import settings


class HealthCheckConfig(AppConfig):
    name = 'health_check.contrib.celery'

    def ready(self):
        from .backends import CeleryHealthCheck

        # Default queue
        plugin_dir.register(CeleryHealthCheck)

        # Other queues defined in SETTINGS:
        for queue, queue_display_name in settings.CELERY_QUEUES.items():
            celery_class_name = 'CeleryHealthCheck' + queue.title()
            CeleryHealthCheckQueue = type(celery_class_name, (CeleryHealthCheck, ), {'queue': queue, 'queue_display_name': queue_display_name})
            plugin_dir.register(CeleryHealthCheckQueue)
