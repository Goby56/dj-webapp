# Generated by Django 4.1.7 on 2023-03-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0006_alter_content_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, max_length=200, upload_to='images'),
        ),
    ]
