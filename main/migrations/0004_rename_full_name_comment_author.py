# Generated by Django 5.1.3 on 2024-11-19 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='full_name',
            new_name='author',
        ),
    ]
