# Generated by Django 4.0 on 2022-09-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=22)),
                ('email', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=7000)),
            ],
        ),
    ]
