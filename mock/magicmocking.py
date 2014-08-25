from unittest import mock

class DummyClass:
    def hello(self):
        print("Hello world")
        return "OK"

m = mock.MagicMock()
print(m.hello())

dummy_object = DummyClass()
spy = mock.MagicMock(wraps=dummy_object)
print(spy.hello())

print(spy[3])
