# Generated by Django 3.2.7 on 2021-10-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20211002_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentermodel',
            name='renter_date',
            field=models.CharField(default='', max_length=30),
        ),
    ]
