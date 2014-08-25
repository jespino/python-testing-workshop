import factory
import factory.fuzzy
import app

class UserFactory(factory.Factory):
    class Meta:
        model = app.User

    first_name = "John"
    last_name = "Doe"
    email = "john@doe.com"


class ProfileFactory(factory.Factory):
    class Meta:
        model = app.Profile

    age = factory.fuzzy.FuzzyInteger(0, 65)
    sex = factory.Iterator([True, False])


class UserSequenceFactory(factory.Factory):
    class Meta:
        model = app.User

    first_name = factory.Sequence(lambda n: "name-{}".format(n))
    last_name = factory.Sequence(lambda n: "surname-{}".format(n))
    email = factory.LazyAttribute(lambda obj: "{}.{}@example.com".format(obj.first_name, obj.last_name))
    profile = factory.SubFactory(ProfileFactory)
