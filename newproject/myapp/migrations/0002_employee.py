# Generated by Django 3.2.7 on 2021-09-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
            ],
        ),
    ]
