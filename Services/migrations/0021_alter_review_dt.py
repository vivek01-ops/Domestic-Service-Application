# Generated by Django 5.1.1 on 2024-10-05 17:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0020_alter_review_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='dt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]