# Generated by Django 3.1.6 on 2021-02-20 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_account_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='User',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created_at']},
        ),
    ]
