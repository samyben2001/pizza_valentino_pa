# Generated by Django 3.2.12 on 2022-05-30 11:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_alter_pizza_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, size=[50, 50], upload_to=''),
        ),
    ]
