# Generated by Django 2.1.4 on 2019-01-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20181228_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dayChosen',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='response',
            name='freeTime',
            field=models.CharField(max_length=2048),
        ),
    ]