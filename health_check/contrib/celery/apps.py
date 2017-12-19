from django.apps import AppConfig

from health_check.plugins import plugin_dir
from django.conf import settings


class HealthCheckConfig(AppConfig):
    name = 'health_check.contrib.celery'

    def ready(self):
        from .backends import CeleryHealthCheck

        # Celery queues defined in SETTINGS as CELERY_QUEUES:
        for queue, queue_dict in settings.CELERY_QUEUES.items():
            celery_class_name = 'CeleryHealthCheck' + queue.title()

            try:
                name = queue_dict['display_name']
            except:
                name = celery_class_name

            # Apply_async will timeout if we pass it a 'default' queue
            # Rather, it should take NoneType
            if queue == 'default':
                queue = None

            CeleryHealthCheckQueue = type(celery_class_name,
                                          (CeleryHealthCheck,),
                                          {'queue_display_name': name, 'queue': queue})
            plugin_dir.register(CeleryHealthCheckQueue)
