# Generated by Django 4.2 on 2023-05-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('mobile_no', models.CharField(max_length=15)),
                ('email_id', models.CharField(max_length=100)),
            ],
        ),
    ]
