# Generated by Django 5.0.3 on 2024-03-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_meep_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meep',
            name='title',
            field=models.CharField(default='No Title', max_length=255),
        ),
    ]