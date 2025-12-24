from .models import DealerLocation, Car, Version, Feature
from django.contrib.auth.models import User

def seed_data():
    # Only seed if no data exists
    if DealerLocation.objects.exists():
        return
    # Create dealer locations
    dealer_location_1 = DealerLocation.objects.create(
        name='ABC Dealership',
        address='123 Main St',
        city='Anytown',
        state='AR-B',
        zip_code='12345',
        phone_number='1234567890',
        email='abc@dealership.com',
        website='http://www.abcdealership.com'
    )

    dealer_location_2 = DealerLocation.objects.create(
        name='XYZ Dealership',
        address='456 Main St',
        city='Anytown',
        state='AR-B',
        zip_code='12345',
        phone_number='1234567890',
        email='xyz@dealership.com',
        website='http://www.xyzdealership.com'
    )

    dealer_location_3 = DealerLocation.objects.create(
        name='123 Dealership',
        address='789 Main St',
        city='Anytown',
        state='AR-B',
        zip_code='12345',
        phone_number='1234567890',
        email='123@dealership.com',
        website='http://www.123dealership.com'
    )

    dealer_location_4 = DealerLocation.objects.create(
        name='456 Dealership',
        address='101 Main St',
        city='Anytown',
        state='AR-B',
        zip_code='12345',
        phone_number='1234567890',
        email='456@dealership.com',
        website='http://www.456dealership.com'
    )

    # Create cars
    car_1 = Car.objects.create(
        make='Toyota',
        model='Camry',
        year=2022,
        description='Reliable and efficient sedan',
        image='car_images/camry.jpeg'
    )

    car_2 = Car.objects.create(
        make='Toyota',
        model='Corolla',
        year=2022,
        description='Compact and fuel-efficient sedan',
        image='car_images/corolla.png'
    )

    car_3 = Car.objects.create(
        make='Toyota',
        model='Crown',
        year=2022,
        description='Luxury sedan',
        image='car_images/crown.png'
    )

    car_4 = Car.objects.create(
        make='Toyota',
        model='Etios',
        year=2022,
        description='Affordable and practical sedan',
        image='car_images/etios.png'
    )

    car_5 = Car.objects.create(
        make='Toyota',
        model='GR86',
        year=2022,
        description='Sports car',
        image='car_images/gr86.png'
    )

    car_6 = Car.objects.create(
        make='Toyota',
        model='SW4',
        year=2022,
        description='SUV',
        image='car_images/sw4.png'
    )

    # Create versions
    version_1 = Version.objects.create(
        name='LE',
        price=25000.00,
        car=car_1,
        description='Base model'
    )

    version_2 = Version.objects.create(
        name='SE',
        price=28000.00,
        car=car_1,
        description='Mid-level model'
    )

    # Create features
    feature_1 = Feature.objects.create(
        name='Sunroof',
        description='Panoramic sunroof',
        version=version_2
    )

    feature_2 = Feature.objects.create(
        name='Leather Seats',
        description='Leather-trimmed seats',
        version=version_2
    )


    # Create User
    user = User.objects.create_user(
        username='admin',
        password='admin123',
        is_staff=True,
        is_superuser=True
    )

    user2 = User.objects.create_user(
        username='user',
        password='user123',
        is_staff=False,
        is_superuser=False
    )

    user3 = User.objects.create_user(
        username='staff',
        password='staff123',
        is_staff=True,
        is_superuser=False
    )

    print('Data seeded successfully')