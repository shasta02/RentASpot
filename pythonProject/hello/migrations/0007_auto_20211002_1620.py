# Generated by Django 3.2.7 on 2021-10-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20211002_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentermodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='rentermodel',
            name='renter_location',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
