# Generated by Django 4.1.7 on 2023-03-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publishing", "0004_alter_content_image_alter_content_snippet_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content_type",
            field=models.CharField(
                choices=[("SNIPPET", "Snippet"), ("IMAGE", "Image"), ("TEXT", "Text")],
                max_length=100,
            ),
        ),
    ]
