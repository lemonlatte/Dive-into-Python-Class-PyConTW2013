

class prop(object):
    def __init__(self, get_func, set_func=None, del_func=None):
        self.get_func = get_func
        self.set_func = set_func
        self.del_func = del_func

    def __get__(self, instance, owner):
        return self.get_func(instance)

    def __set__(self, instance, value):
        if hasattr(self, "set_func"):
            self.set_func(instance, value)

    def __del__(self, instance):
        if hasattr(self, "del_func"):
            self.del_func(instance)


class Number(object):

    def __init__(self):
        self._postive_number = 0

    def setPostiveNumber(self, value):
        if value >= 0:
            self._postive_number = value
        else:
            raise ValueError("Number must greater than 0")

    def getPostiveNumber(self):
        if hasattr(self, "_postive_number"):
            return self._postive_number
        else:
            return None
    postive_number = prop(getPostiveNumber, setPostiveNumber)
