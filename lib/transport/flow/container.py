import os

_container_instance = {}
_context_module = None


def get_container(module=None, context_name='AppContext', force_new=False):
    global _container_instance, _context_module
    context_name = os.getenv('APP_CONTEXT', context_name)
    container_id = context_name
    if _container_instance.get(container_id) and not force_new:
        return _container_instance.get(container_id)

    if not _context_module:
        if not module:
            import app_context
            _context_module = app_context
        else:
            _context_module = module

    context = getattr(_context_module, context_name)
    from springpython.context import ApplicationContext
    _container_instance[container_id] = ApplicationContext(context())
    return _container_instance.get(container_id)
