from django.apps import AppConfig
from django.conf import settings

from health_check.plugins import plugin_dir


class HealthCheckConfig(AppConfig):
    name = 'health_check.contrib.celery'

    def ready(self):
        from .backends import CeleryHealthCheck

        # Celery queues defined in SETTINGS as CELERY_QUEUES:
        for queue, queue_dict in settings.CELERY_QUEUES.items():
            celery_class_name = 'CeleryHealthCheck' + queue.title()

            try:
                name = queue_dict['display_name']
            except KeyError:
                name = celery_class_name

            celery_class = type(celery_class_name, (CeleryHealthCheck,), {'queue_display_name': name, 'queue': queue})

            # Register the celery health check under /ht/
            plugin_dir.register(celery_class)
            # Register the celery health check under its custom url /ht/celery_{queue_name}
            # Allow specifying the registry name
            registry_name = '_registry%s' % queue
            plugin_dir.register(celery_class, registry=registry_name)
