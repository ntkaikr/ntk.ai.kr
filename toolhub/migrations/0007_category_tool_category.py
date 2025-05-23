# Generated by Django 5.2 on 2025-04-25 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolhub', '0006_tool_creators'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': '카테고리',
            },
        ),
        migrations.AddField(
            model_name='tool',
            name='category',
            field=models.ForeignKey(blank=True, help_text='이 도구가 속한 카테고리', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tools', to='toolhub.category'),
        ),
    ]
