# Generated by Django 2.2.1 on 2019-05-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simel', '0006_remove_movimiento_coment'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='coment',
            field=models.CharField(default='Movimiento', max_length=150, verbose_name='comentario'),
        ),
    ]