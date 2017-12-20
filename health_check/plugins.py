class AlreadyRegistered(Exception):
    pass


class NotRegistered(Exception):
    pass


class HealthCheckPluginDirectory:
    """Django health check registry."""

    def __init__(self):
        self._registry = []  # plugin_class class -> plugin options

    def reset(self):
        """Reset registry state, e.g. for testing purposes."""
        self._registry = []

    def register(self, plugin, registry='_registry', **options):
        """Add the given plugin from the registry."""
        # Instantiate the admin class to save in the registry
        try:
            reg = getattr(self, registry)
        except AttributeError:
            setattr(self, registry, [])
            reg = getattr(self, registry)

        reg.append((plugin, options))


plugin_dir = HealthCheckPluginDirectory()
