# Generated by Django 4.2.3 on 2023-07-24 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_app', '0003_alter_account_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
