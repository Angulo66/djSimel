# Generated by Django 2.2.1 on 2019-05-26 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simel', '0005_auto_20190526_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento',
            name='coment',
        ),
    ]