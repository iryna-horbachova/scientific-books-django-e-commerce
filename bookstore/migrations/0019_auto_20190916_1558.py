# Generated by Django 2.2.3 on 2019-09-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0018_promocode_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='percentage',
            field=models.IntegerField(default=10),
        ),
    ]
