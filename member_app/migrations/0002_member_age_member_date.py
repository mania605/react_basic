# Generated by Django 5.1.2 on 2024-10-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
