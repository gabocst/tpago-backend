# Generated by Django 2.0.5 on 2019-04-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]
