# Generated by Django 2.1.5 on 2019-03-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_doctor_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False, verbose_name='patient status'),
        ),
    ]
