# Generated by Django 5.0.2 on 2024-03-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=200)),
                ('vehicle_regNo', models.IntegerField()),
                ('vehicle_owner', models.CharField(max_length=100)),
            ],
        ),
    ]
