# Generated by Django 4.2.3 on 2023-08-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sage', models.IntegerField()),
            ],
        ),
    ]
