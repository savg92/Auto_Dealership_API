# Generated by Django 5.0.6 on 2024-05-08 04:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images')),
            ],
        ),
        migrations.CreateModel(
            name='DealerLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AR-A', 'Salta'), ('AR-B', 'Buenos Aires Province'), ('AR-C', 'Autonomous City of Buenos Aires'), ('AR-D', 'San Luis'), ('AR-E', 'Entre Ríos'), ('AR-F', 'La Rioja'), ('AR-G', 'Santiago del Estero'), ('AR-H', 'Chaco'), ('AR-J', 'San Juan'), ('AR-K', 'Catamarca'), ('AR-L', 'La Pampa'), ('AR-M', 'Mendoza'), ('AR-N', 'Misiones'), ('AR-P', 'Formosa'), ('AR-Q', 'Neuquén'), ('AR-R', 'Río Negro'), ('AR-S', 'Santa Fe'), ('AR-T', 'Tucumán'), ('AR-U', 'Chubut'), ('AR-V', 'Tierra del Fuego'), ('AR-W', 'Corrientes'), ('AR-X', 'Córdoba'), ('AR-Y', 'Jujuy'), ('AR-Z', 'Santa Cruz')], max_length=100)),
                ('zip_code', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{5}(?:[-\\s]\\d{4})?$', message='Invalid zip code format')])),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?\\d{9,15}$', message='Invalid phone number format')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='api.car')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='api.version')),
            ],
        ),
    ]
