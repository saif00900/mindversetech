# Generated by Django 4.0 on 2022-09-15 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=40)),
                ('about', models.CharField(max_length=700)),
                ('Link4btn', models.CharField(max_length=5000)),
                ('other', models.CharField(max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='Portfolio/')),
                ('field', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Icon1', models.CharField(max_length=40)),
                ('Icon2', models.CharField(max_length=40)),
                ('Icon3', models.CharField(max_length=40)),
                ('Icon4', models.CharField(max_length=40)),
                ('Icon5', models.CharField(max_length=40)),
                ('Icon6', models.CharField(max_length=40)),
                ('Icon1Desc', models.CharField(max_length=600)),
                ('Icon2Desc', models.CharField(max_length=600)),
                ('Icon3Desc', models.CharField(max_length=600)),
                ('Icon4Desc', models.CharField(max_length=600)),
                ('Icon5Desc', models.CharField(max_length=600)),
                ('Icon6Desc', models.CharField(max_length=600)),
            ],
        ),
    ]