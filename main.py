from faker import Faker
fake = Faker('en_CA')
for _ in range(10):
    print(fake.name())