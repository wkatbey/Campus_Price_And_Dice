# Generated by Django 2.1.7 on 2019-03-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0002_user_favorite_restaurant_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='items',
            field=models.ManyToManyField(to='campus.Item'),
        ),
    ]
