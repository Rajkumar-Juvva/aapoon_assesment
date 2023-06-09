# Generated by Django 4.1.7 on 2023-03-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeachersInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, null=True)),
                ('second_name', models.TextField(blank=True, null=True)),
                ('profile_picture', models.TextField(blank=True, null=True)),
                ('email_address', models.TextField(blank=True, null=True, unique=True)),
                ('phone_number', models.TextField(blank=True, null=True)),
                ('room_number', models.TextField(blank=True, null=True)),
                ('subjects_taught', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
