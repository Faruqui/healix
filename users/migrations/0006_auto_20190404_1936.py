# Generated by Django 2.1.5 on 2019-04-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190316_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='education',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
