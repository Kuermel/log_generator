from springpython.config import PythonConfig
from springpython.config import Object


class AppContext(PythonConfig):
    @Object(lazy_init=True)
    def zookeeper(self):
        import zookeeper
        return zookeeper.get()
