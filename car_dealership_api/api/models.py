from django.db import models
from django.core.validators import RegexValidator

class DealerLocation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=100,
        choices=[
            ('', 'Select a state'),
            ('AR-A', 'Salta'),
            ('AR-B', 'Buenos Aires Province'),
            ('AR-C', 'Autonomous City of Buenos Aires'),
            ('AR-D', 'San Luis'),
            ('AR-E', 'Entre Ríos'),
            ('AR-F', 'La Rioja'),
            ('AR-G', 'Santiago del Estero'),
            ('AR-H', 'Chaco'),
            ('AR-J', 'San Juan'),
            ('AR-K', 'Catamarca'),
            ('AR-L', 'La Pampa'),
            ('AR-M', 'Mendoza'),
            ('AR-N', 'Misiones'),
            ('AR-P', 'Formosa'),
            ('AR-Q', 'Neuquén'),
            ('AR-R', 'Río Negro'),
            ('AR-S', 'Santa Fe'),
            ('AR-T', 'Tucumán'),
            ('AR-U', 'Chubut'),
            ('AR-V', 'Tierra del Fuego'),
            ('AR-W', 'Corrientes'),
            ('AR-X', 'Córdoba'),
            ('AR-Y', 'Jujuy'),
            ('AR-Z', 'Santa Cruz'),
        ]
    )
    zip_code = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{5}(?:[-\s]\d{4})?$', message='Invalid zip code format')]
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message='Invalid phone number format')]
    )
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='car_images', blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Version(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='versions')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.car} - {self.name}"

class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='features')

    def __str__(self):
        return self.name