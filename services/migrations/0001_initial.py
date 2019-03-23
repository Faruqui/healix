# Generated by Django 2.1.7 on 2019-03-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eprescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('days', models.IntegerField(null=True)),
                ('comment', models.TextField(null=True)),
                ('after_breakfrist', models.BooleanField()),
                ('after_lunch', models.BooleanField()),
                ('after_dinner', models.BooleanField()),
                ('before_breakfrist', models.BooleanField()),
                ('before_lunch', models.BooleanField()),
                ('before_dinner', models.BooleanField()),
            ],
        ),
    ]