# Generated by Django 4.2.1 on 2023-06-05 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_is_active_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_email',
            new_name='user',
        ),
    ]
