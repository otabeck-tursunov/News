# Generated by Django 5.1.3 on 2024-11-19 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_news_categories_news_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='categories',
            new_name='category',
        ),
    ]
