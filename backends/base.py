from abc import abstractmethod


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseTargetBackend:
    """Abstract target backend"""

    # We should't really need more than one instance of a backend
    __metaclass__ = Singleton

    @abstractmethod
    def __init__(self, app):
        """Configure from app config"""
        pass

    @abstractmethod
    def redispatch(self, data):
        """Redispatch passed data to target"""
        pass

    @abstractmethod
    def get_target_name(self):
        """Get target name"""
        pass

    @abstractmethod
    def is_ready(self):
        """Backend initialized properly"""
        pass
