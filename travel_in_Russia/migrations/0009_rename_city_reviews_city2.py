# Generated by Django 4.1.7 on 2023-03-26 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_in_Russia', '0008_rename_review_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='city',
            new_name='city2',
        ),
    ]