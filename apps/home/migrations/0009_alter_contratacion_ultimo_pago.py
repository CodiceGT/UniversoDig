# Generated by Django 4.2.1 on 2023-06-21 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_contratacion_ultimo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratacion',
            name='ultimo_pago',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]