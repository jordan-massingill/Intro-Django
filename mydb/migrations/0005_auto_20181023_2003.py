# Generated by Django 2.1.2 on 2018-10-23 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0004_shelterdog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shelterdog',
            old_name='shelter',
            new_name='city',
        ),
    ]