# Generated by Django 3.2.12 on 2022-05-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_alter_pates_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]