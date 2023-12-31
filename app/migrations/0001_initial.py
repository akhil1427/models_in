# Generated by Django 4.2.6 on 2023-12-11 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='county',
            fields=[
                ('C_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital_name', models.CharField(max_length=20)),
                ('county_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.county')),
            ],
        ),
    ]
