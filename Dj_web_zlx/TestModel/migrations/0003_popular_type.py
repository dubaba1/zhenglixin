# Generated by Django 2.0 on 2019-04-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_auto_20190410_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='popular_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=20)),
                ('freq', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
