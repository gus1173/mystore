# Generated by Django 5.0.3 on 2024-04-24 07:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cart_reviews'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Carts',
        ),
    ]
