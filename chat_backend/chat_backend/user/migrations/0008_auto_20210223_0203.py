# Generated by Django 3.1.6 on 2021-02-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210222_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-user_type']},
        ),
        migrations.AddField(
            model_name='user',
            name='room_uuid',
            field=models.CharField(default='NULL', max_length=254, null=True, verbose_name='방 uuid'),
        ),
    ]