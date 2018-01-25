class Test:
    test23 = "static"

    def __init__(self):
        pass

    @classmethod
    def test(cls):
        return "hello"

    @property
    def test3(self):

        return self.test() + self.test2()

    def test2(self):
        return "hi"



Test.test()
