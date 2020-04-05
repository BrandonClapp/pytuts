class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23 # Single underscore prefix. Mostly convention, treated as private class member
        self.__baz = 42 # Python will take __ and mangle the name to _Test__baz. 

class SubTest(Test):
    def __init__(self):
        self._bar = 20

t = Test()
t2 = SubTest()

print(t.foo) # "public" member
print(t._bar) # convention based to mean "private"
# t.__baz does not exist.
t._Test__baz # don't access it like this.

print(t2._bar) # 20, because subclass redefined it
