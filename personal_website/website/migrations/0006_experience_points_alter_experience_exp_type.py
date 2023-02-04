# Generated by Django 4.1.5 on 2023-01-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_experience_exp_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='points',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='experience',
            name='exp_type',
            field=models.CharField(choices=[('W', 'Working'), ('E', 'Education')], default='W', max_length=1),
        ),
    ]