# Generated by Django 4.1.5 on 2023-01-14 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_export_db', '0002_remove_employee_empcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Name',
            new_name='Navn',
        ),
    ]
