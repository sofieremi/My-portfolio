# Generated by Django 4.0 on 2022-01-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_human'),
    ]

    operations = [
        migrations.CreateModel(
            name='Huggy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
    ]