# Generated by Django 3.2.12 on 2023-04-03 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0027_auto_20230403_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergene',
            options={'verbose_name_plural': '02. Allergènes'},
        ),
        migrations.AlterModelOptions(
            name='annonce',
            options={'verbose_name_plural': '08. Annonces'},
        ),
        migrations.AlterModelOptions(
            name='boisson',
            options={'verbose_name_plural': '07. Boissons'},
        ),
        migrations.AlterModelOptions(
            name='dessert',
            options={'verbose_name_plural': '06. Desserts'},
        ),
        migrations.AlterModelOptions(
            name='entree',
            options={'verbose_name_plural': '03. Entrées'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name_plural': '01. Ingrédients'},
        ),
        migrations.AlterModelOptions(
            name='pates',
            options={'verbose_name_plural': '05. Pâtes'},
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': '04. Pizzas'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': '09. Services'},
        ),
    ]
