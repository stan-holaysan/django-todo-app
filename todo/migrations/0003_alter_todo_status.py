# Generated by Django 4.2.16 on 2024-11-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_details_todo_llm_response_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
