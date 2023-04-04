# Generated by Django 3.2.12 on 2023-04-03 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0026_alter_pizza_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergene',
            options={'verbose_name_plural': '2. Allergènes'},
        ),
        migrations.AlterModelOptions(
            name='annonce',
            options={'verbose_name_plural': '8. Annonces'},
        ),
        migrations.AlterModelOptions(
            name='boisson',
            options={'verbose_name_plural': '7. Boissons'},
        ),
        migrations.AlterModelOptions(
            name='dessert',
            options={'verbose_name_plural': '6. Desserts'},
        ),
        migrations.AlterModelOptions(
            name='entree',
            options={'verbose_name_plural': '3. Entrées'},
        ),
        migrations.AlterModelOptions(
            name='horaire',
            options={'ordering': ['pk'], 'verbose_name_plural': '10. Horaire'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name_plural': '1. Ingrédients'},
        ),
        migrations.AlterModelOptions(
            name='pates',
            options={'verbose_name_plural': '5. Pâtes'},
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name_plural': '4. Pizzas'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': '9. Services'},
        ),
    ]
