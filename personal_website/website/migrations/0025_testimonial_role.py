# Generated by Django 4.1.5 on 2023-02-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_testimonial_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='role',
            field=models.CharField(default='', max_length=50),
        ),
    ]
