class AttrTest(object):
    def __getattribute__(self, name):
        if name in ["test"]:
            return "Return by __getattribute__"
        raise AttributeError

    def __getattr__(self, name):
        return "You are finding a missing variable:", name


class AttrOldTest:
    def __getattribute__(self, name):
        return "Go through __getattribute__"

    def __getattr__(self, name):
        return "You are finding a missing variable:", name

if __name__ == '__main__':
    i = raw_input("1) Use new-style class\n2) Use classic class\n")

    try:
        choice = int(i)
    except:
        raise ValueError("Unavailable choice.")

    if choice == 1:
        cls = AttrTest
    elif choice == 2:
        cls = AttrOldTest
    else:
        raise ValueError("Unavailable choice.")

    print "instance = %s()" % cls.__name__
    instance = cls()
    print "Get instance.test"
    print instance.test
    print "Get instance.other"
    print instance.other
