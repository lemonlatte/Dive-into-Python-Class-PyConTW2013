

class SimulateClassMethod(object):
    def __init__(self, f):
        self._func = f

    def __get__(self, instance, owner):
        if instance:
            print "A instance want to call the method."
            return self._func.__get__(instance, owner)
        else:
            print "A class want to call the method."
            return self._func.__get__(owner, owner)


class Host(object):

    desc = "This is a host."

    def __init__(self, name, os):
        pass

    def _cls_method_test(cls, name):
        print cls.desc

    cls_method = SimulateClassMethod(_cls_method_test)
