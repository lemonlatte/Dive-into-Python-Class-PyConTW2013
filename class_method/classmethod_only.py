

class TargetError(Exception):
    """Base class for exceptions in this module."""
    pass


class ClassMethodOnly(object):
    def __init__(self, f):
        self._func = f

    def __get__(self, instance, owner):
        if instance:
            raise TargetError("This method can not be called by an instance.")
        else:
            return self._func.__get__(owner, owner)


class Host(object):

    desc = "This is a host."

    def __init__(self, name, os):
        self.name = name
        self.os = os

    def _from_windows(cls, name):
        return cls(name, "Windows")

    from_windows = ClassMethodOnly(_from_windows)
