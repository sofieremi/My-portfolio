# Generated by Django 4.0 on 2022-01-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_huggy'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.IntegerField()),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Huggy',
        ),
    ]
