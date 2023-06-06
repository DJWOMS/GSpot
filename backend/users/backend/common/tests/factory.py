import factory
from common.models import Country, ContactType


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Faker("country")


class ContactTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactType

    name = factory.Faker("word")
