# Generated by Django 4.2 on 2023-04-16 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='Contact Phine'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Website Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='wemail_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
    ]