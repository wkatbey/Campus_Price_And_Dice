# Generated by Django 2.2 on 2019-05-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0015_auto_20190503_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Tell us abbout your restaurant!'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='(Primary) Phone Number'),
        ),
    ]
