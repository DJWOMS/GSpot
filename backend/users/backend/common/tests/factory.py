import factory
from administrator.models import Admin
from common.models import ContactType, Country
from customer.models import CustomerUser
from developer.models import CompanyUser


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Faker("country")


class ContactTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContactType

    name = factory.Faker("word")


class BaseUserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    username = factory.Faker('lexify', text='??????????')
    phone = factory.Faker('random_number', digits=10)
    avatar = ''
    is_banned = False
    is_active = True


class AdminUserFactory(BaseUserFactory):
    class Meta:
        model = Admin

    is_superuser = False


class CustomerUserFactory(BaseUserFactory):
    class Meta:
        model = CustomerUser

    birthday = factory.Faker('date_object')


class DeveloperUserFactory(BaseUserFactory):
    class Meta:
        model = CompanyUser

    is_superuser = False


class UsersFactory:
    user_types = {
        'admin': AdminUserFactory,
        'su_admin': AdminUserFactory,
        'customer': CustomerUserFactory,
        'developer': DeveloperUserFactory,
        'su_developer': DeveloperUserFactory,
    }

    @classmethod
    def get_user(cls, user_type: str) -> dict:
        if user_type not in cls.user_types:
            raise KeyError("Unknown user type!")
        obj = cls.uses_types.get(user_type)
        return obj(is_superuser=True) if user_type.startswith('su') else obj()


__all__ = ['AdminUserFactory', 'CustomerUserFactory', 'DeveloperUserFactory', 'UsersFactory']
