# Generated by Django 5.2 on 2025-04-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_remove_todo_due_date_todo_due_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
