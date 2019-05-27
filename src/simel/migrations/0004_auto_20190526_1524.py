# Generated by Django 2.2.1 on 2019-05-26 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simel', '0003_auto_20190525_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='coment',
            field=models.CharField(default='hola so yo defualt', max_length=150, verbose_name='comentario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aduedo',
            name='adeudo',
            field=models.BinaryField(verbose_name='aduedo de libro'),
        ),
        migrations.AlterField(
            model_name='aduedo',
            name='matRC',
            field=models.IntegerField(verbose_name='materias cursadando en RC'),
        ),
        migrations.AlterField(
            model_name='aduedo',
            name='numControl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simel.Alumno', verbose_name='numero de control'),
        ),
    ]