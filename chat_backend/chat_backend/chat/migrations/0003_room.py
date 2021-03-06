# Generated by Django 3.1.6 on 2021-02-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0002_auto_20210221_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100, verbose_name='방이름')),
                ('number', models.IntegerField(verbose_name='방번호')),
                ('status', models.CharField(max_length=30, verbose_name='방 상태')),
                ('uuid', models.CharField(max_length=254, verbose_name='방 uuid')),
            ],
        ),
    ]