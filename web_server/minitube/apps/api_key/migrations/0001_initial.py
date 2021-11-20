# Generated by Django 3.2.9 on 2021-11-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('key', models.TextField()),
                ('key_config', models.JSONField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
