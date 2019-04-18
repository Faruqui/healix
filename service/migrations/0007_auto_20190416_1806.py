# Generated by Django 2.1.7 on 2019-04-16 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190412_2040'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0006_remove_prescription_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='users.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='area',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Location'),
        ),
    ]