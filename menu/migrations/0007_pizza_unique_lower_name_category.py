# Generated by Django 3.2.12 on 2022-02-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20220222_1355'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='pizza',
            constraint=models.UniqueConstraint(fields=('nom',), name='unique_lower_name_category'),
        ),
    ]