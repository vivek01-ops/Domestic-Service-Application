# Generated by Django 4.0.5 on 2023-03-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_alter_cleaning_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaning',
            name='offer',
            field=models.CharField(default='', max_length=50),
        ),
    ]