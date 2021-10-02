# Generated by Django 3.2.7 on 2021-10-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_alter_renterspots_spots_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spots_available', models.CharField(max_length=3)),
                ('renter_price', models.CharField(max_length=6)),
                ('renter_location', models.CharField(max_length=5)),
                ('timing_options', models.CharField(choices=[('0', '12am-1am'), ('1', '1am-2am'), ('2', '2am-3am'), ('3', '3am-4am'), ('4', '4am-5am'), ('5', '5am-6am'), ('6', '6am-7am'), ('7', '7am-8am'), ('8', '8am-9am'), ('9', '9am-10am'), ('10', '10am-11am'), ('11', '11am-12pm'), ('12', '12pm-1pm'), ('13', '1pm-2pm'), ('14', '2pm-3pm'), ('15', '3pm-4pm'), ('16', '4pm-5pm'), ('17', '5pm-6pm'), ('18', '6pm-7pm'), ('19', '7pm-8pm'), ('20', '8pm-9pm'), ('21', '9pm-10pm'), ('22', '10pm-11pm'), ('23', '11pm-12am')], default='', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='RenterLocation',
        ),
        migrations.DeleteModel(
            name='RenterPrice',
        ),
        migrations.DeleteModel(
            name='RenterSpots',
        ),
        migrations.DeleteModel(
            name='RenterTimings',
        ),
    ]
