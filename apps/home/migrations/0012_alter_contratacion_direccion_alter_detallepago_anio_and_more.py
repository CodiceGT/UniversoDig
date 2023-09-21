# Generated by Django 4.2.5 on 2023-09-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_contratacion_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratacion',
            name='direccion',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='detallepago',
            name='anio',
            field=models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=4),
        ),
        migrations.AlterField(
            model_name='detallepago',
            name='mes',
            field=models.CharField(choices=[('1', 'Enero'), ('2', 'Febrero'), ('3', 'Marzo'), ('4', 'Abril'), ('5', 'Mayo'), ('6', 'Junio'), ('7', 'Julio'), ('8', 'Agosto'), ('9', 'Septiembre'), ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')], max_length=2),
        ),
        migrations.AlterField(
            model_name='informacion',
            name='logo',
            field=models.ImageField(blank=True, upload_to='logo'),
        ),
        migrations.DeleteModel(
            name='Anio',
        ),
        migrations.DeleteModel(
            name='Mes',
        ),
    ]