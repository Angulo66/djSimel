# Generated by Django 2.2.1 on 2019-05-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simel', '0004_auto_20190526_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='coment',
            field=models.CharField(default='Movimiento', max_length=150, verbose_name='comentario'),
        ),
    ]