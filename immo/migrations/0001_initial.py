# Generated by Django 2.2.7 on 2019-11-14 17:43

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
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos')),
                ('description', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('is_mvp', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Immo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('photo_main', models.ImageField(upload_to='photos')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='immo.Realtor')),
            ],
        ),
    ]
