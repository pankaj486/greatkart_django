# Generated by Django 3.1 on 2021-08-26 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tex',
            new_name='tax',
        ),
    ]
