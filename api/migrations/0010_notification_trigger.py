# Generated by Django 3.1.3 on 2020-11-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_notification_opened'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='trigger',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
