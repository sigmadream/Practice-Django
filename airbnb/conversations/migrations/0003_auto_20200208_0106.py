# Generated by Django 3.0a1 on 2020-02-07 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0002_auto_20200208_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converstation',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='converstation', to=settings.AUTH_USER_MODEL),
        ),
    ]
