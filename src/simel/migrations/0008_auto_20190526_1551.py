# Generated by Django 2.2.1 on 2019-05-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simel', '0007_movimiento_coment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='coment',
            field=models.CharField(blank=True, default='Creo Solicitud', max_length=320, null=True, verbose_name='comentario'),
        ),
    ]
