# Generated by Django 3.1.1 on 2020-10-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20201007_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='isRate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='note',
            field=models.TextField(default='Your request is under reviews by canadian', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='rate',
            field=models.IntegerField(default=3),
        ),
    ]
