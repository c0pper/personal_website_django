# Generated by Django 4.1.5 on 2023-02-02 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_certification_alter_institution_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='link',
            new_name='url',
        ),
    ]
