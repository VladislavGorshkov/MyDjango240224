# Generated by Django 5.0.2 on 2024-03-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='info',
            field=models.CharField(default='No info', max_length=100),
            preserve_default=False,
        ),
    ]
