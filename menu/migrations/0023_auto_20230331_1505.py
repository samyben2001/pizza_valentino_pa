# Generated by Django 3.2.12 on 2023-03-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0022_auto_20220606_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('actif', models.BooleanField()),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
                ('annonce', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('debut', models.TimeField()),
                ('fin', models.TimeField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='service',
            constraint=models.UniqueConstraint(fields=('nom',), name='unique_services_name'),
        ),
        migrations.AddField(
            model_name='horaire',
            name='services',
            field=models.ManyToManyField(blank=True, to='menu.Service'),
        ),
        migrations.AddConstraint(
            model_name='annonce',
            constraint=models.UniqueConstraint(fields=('nom',), name='unique_annonce_name'),
        ),
        migrations.AddConstraint(
            model_name='horaire',
            constraint=models.UniqueConstraint(fields=('jour',), name='unique_horaire_name'),
        ),
    ]
