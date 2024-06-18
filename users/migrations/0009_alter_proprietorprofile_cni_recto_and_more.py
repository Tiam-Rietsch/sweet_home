# Generated by Django 5.0.6 on 2024-06-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_buyerprofile_user_alter_proprietorprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proprietorprofile',
            name='cni_recto',
            field=models.ImageField(blank=True, null=True, upload_to='cni_recto/'),
        ),
        migrations.AlterField(
            model_name='proprietorprofile',
            name='cni_verso',
            field=models.ImageField(blank=True, null=True, upload_to='cni_verso/'),
        ),
        migrations.AlterField(
            model_name='proprietorprofile',
            name='facture_recto',
            field=models.ImageField(blank=True, null=True, upload_to='bill_recto/'),
        ),
        migrations.AlterField(
            model_name='proprietorprofile',
            name='facture_verso',
            field=models.ImageField(blank=True, null=True, upload_to='bill_verso/'),
        ),
    ]
