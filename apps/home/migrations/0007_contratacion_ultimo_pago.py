# Generated by Django 4.2.1 on 2023-06-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_contratacion_estado_reportefallo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratacion',
            name='ultimo_pago',
            field=models.DateField(auto_now=True),
        ),
    ]