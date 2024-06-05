from .models import DealerLocation, Car, Version, Feature

def seed_data():
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

    # Create cars
    car_1 = Car.objects.create(
        make='Toyota',
        model='Camry',
        year=2022,
        description='Reliable and efficient sedan'
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