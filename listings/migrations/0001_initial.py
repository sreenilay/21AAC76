# Generated by Django 3.2.5 on 2021-08-19 14:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Mobiles', 'Mobiles'), ('Cars', 'Cars'), ('Electronics', 'Electronics'), ('Property', 'Property'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Fashion', 'Fashion'), ('Jobs', 'Jobs'), ('Bikes', 'Bikes')], max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AS', 'Assam'), ('KA', 'Karnataka'), ('MN', 'Manipur'), ('AP', 'Andhra Pradesh'), ('TN', 'Tamil Nadu'), ('HP', 'Haryana'), ('PB', 'Punjab'), ('NL', 'Nagaland'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('TS', 'Telegana'), ('GJ', 'Gujarat'), ('BR', 'Bihar'), ('JH', 'Jharkhand'), ('WB', 'West Bengal'), ('UK', 'Uttarakhand'), ('OD', 'Odisha'), ('UP', 'Uttar Pradesh'), ('MI', 'Sikkim'), ('MH', 'Maharashtra'), ('KL', 'Kerala'), ('AR', 'Arunachal Pradesh'), ('TR', 'Tripura'), ('MP', 'Madhya Pradesh'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('RJ', 'Rajasthan')], max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('total_rating', models.IntegerField(null=True)),
                ('no_of_rating', models.IntegerField(null=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(default=datetime.datetime.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]