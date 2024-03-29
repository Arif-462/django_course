# Generated by Django 4.2.4 on 2023-08-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('roll', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('section', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
