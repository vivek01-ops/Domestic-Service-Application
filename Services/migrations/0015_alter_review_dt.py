# Generated by Django 4.0.5 on 2023-04-14 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0014_alter_review_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='dt',
            field=models.DateField(default=datetime.date(2023, 4, 14)),
        ),
    ]
