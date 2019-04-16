# Generated by Django 2.1.7 on 2019-04-16 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20190416_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='id',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctors', serialize=False, to='users.Doctor'),
        ),
    ]
