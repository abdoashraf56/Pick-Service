# Generated by Django 3.1.1 on 2020-09-29 11:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200923_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='canadian',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ef45835e-12ca-46c6-bb8e-4b540b265214'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='canadian',
            name='occupation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='canadians', to='myapp.occupation'),
        ),
    ]
