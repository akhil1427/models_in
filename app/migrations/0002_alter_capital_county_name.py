# Generated by Django 4.2.6 on 2023-12-11 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capital',
            name='county_name',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='app.county'),
        ),
    ]