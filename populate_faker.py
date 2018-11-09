import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Django_Faker.settings'

import django

django.setup()

# import model and Faker
from fake_app.models import UserModel
from faker import Faker

fake_generator = Faker()


def populate(N=5):
    for entry in range(N):
        # Now create fake data
        fake_name = fake_generator.name()
        fake_email = fake_generator.email()
        fake_company = fake_generator.company()
        fake_url = fake_generator.url()
        fake_date = fake_generator.date()

        # now entry those data on database
        model_data = UserModel.objects.get_or_create(user_name=fake_name, email=fake_email, website_name=fake_company,
                                                     website_url=fake_url, access_date=fake_date)[0]


if __name__ == '__main__':
    print('POPULATING DATABASE')
    populate(25)
    print("COMPLETE")
