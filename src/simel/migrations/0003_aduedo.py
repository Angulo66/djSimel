# Generated by Django 2.2.1 on 2019-05-16 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simel', '0002_auto_20190516_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aduedo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditosAcum', models.IntegerField(verbose_name='creditos acumulados')),
                ('adeudo', models.BinaryField(default=0, verbose_name='aduedo de libro')),
                ('cantMov', models.IntegerField(verbose_name='cantidad de movilidades curados')),
                ('cursoVerano', models.BinaryField(verbose_name='')),
                ('coment', models.CharField(max_length=320, verbose_name='commentario')),
                ('numControl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simel.Alumno', verbose_name='')),
            ],
        ),
    ]
