# Generated by Django 5.2.1 on 2025-05-11 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carinventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
