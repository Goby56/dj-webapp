# Generated by Django 4.1.7 on 2023-03-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("publishing", "0002_alter_content_image_alter_content_snippet_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="snippet",
            field=models.TextField(
                max_length=2000, null=True, verbose_name="Code Snippet"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="text",
            field=models.TextField(
                max_length=2000, null=True, verbose_name="Plain Text"
            ),
        ),
    ]
