# Generated by Django 3.1.6 on 2021-02-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20210221_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['number']},
        ),
        migrations.AddField(
            model_name='room',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='잠금상태'),
        ),
    ]
