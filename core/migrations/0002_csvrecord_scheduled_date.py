# Generated by Django 2.0.2 on 2018-03-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvrecord',
            name='scheduled_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
