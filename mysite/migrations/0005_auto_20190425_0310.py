# Generated by Django 2.1.7 on 2019-04-25 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190425_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='img/teachers/'),
        ),
    ]
