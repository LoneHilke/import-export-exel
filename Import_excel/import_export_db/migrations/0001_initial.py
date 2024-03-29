# Generated by Django 4.1.5 on 2023-01-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empcode', models.CharField(default='', max_length=10)),
                ('Name', models.CharField(max_length=150, null=True)),
                ('Gruppe', models.CharField(max_length=100, null=True)),
                ('Morgen', models.CharField(max_length=100, null=True)),
                ('Eftermiddag', models.CharField(max_length=30, null=True)),
                ('Ferie', models.CharField(default='', max_length=12, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(default='', max_length=5, null=True)),
                ('qualification', models.CharField(default='', max_length=50, null=True)),
                ('Alder', models.FloatField(default='', max_length=50, null=True)),
            ],
        ),
    ]
