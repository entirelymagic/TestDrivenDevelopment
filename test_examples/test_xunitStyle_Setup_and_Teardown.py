class TestClass:
    @classmethod
    def setup_class(cls):
        print("\nSetup TestClass")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test1!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTeardowning test1!")
        elif method == self.test2:
            print("\nTeardowning test2!")
        else:
            print("\nTeardowning unknown test!")

    def test1(self):
        print("Executing test1")
        assert True

    def test2(self):
        print("Executing test2")
        assert True
