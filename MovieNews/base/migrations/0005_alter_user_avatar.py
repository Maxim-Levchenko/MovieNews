# Generated by Django 3.2.20 on 2023-07-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_moderator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=''),
        ),
    ]
