# Generated by Django 3.1.6 on 2021-02-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210221_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(max_length=100, null=True, verbose_name='방 비밀번호'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='방이름'),
        ),
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(max_length=30, null=True, verbose_name='방 상태'),
        ),
        migrations.AlterField(
            model_name='room',
            name='uuid',
            field=models.CharField(max_length=254, null=True, verbose_name='방 uuid'),
        ),
    ]
