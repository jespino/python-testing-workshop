from unittest import mock

class DummyClass:
    def hello(self):
        print("Hello world")
        return "OK"

m = mock.Mock()
print(m.hello())

dummy_object = DummyClass()
spy = mock.Mock(wraps=dummy_object)
print(spy.hello())

print(spy[3])
