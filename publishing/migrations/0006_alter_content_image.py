# Generated by Django 4.1.7 on 2023-03-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publishing", "0005_alter_post_content_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="image",
            field=models.ImageField(
                blank=True, max_length=200, upload_to="static/images"
            ),
        ),
    ]
