# Generated by Django 5.1.2 on 2024-10-24 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0003_member_age_alter_member_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date',
            field=models.DateField(null=True),
        ),
    ]