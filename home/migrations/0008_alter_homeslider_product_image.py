# Generated by Django 4.1.4 on 2022-12-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homeslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslider',
            name='product_Image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]