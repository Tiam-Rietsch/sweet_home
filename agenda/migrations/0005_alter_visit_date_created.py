# Generated by Django 5.0.6 on 2024-06-20 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_visit_date_created_visit_date_held'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]