# Generated by Django 5.0.6 on 2024-05-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('course', models.CharField(choices=[('BS-CS', 'Computer Science'), ('BS-DS', 'Data Science'), ('BS-IT', 'Information Technology'), ('BS-IS', 'Information Systems')], max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
