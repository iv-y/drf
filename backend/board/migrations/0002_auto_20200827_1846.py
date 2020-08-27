# Generated by Django 3.1 on 2020-08-27 09:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reply',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='liked_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_replies', to=settings.AUTH_USER_MODEL),
        ),
    ]
