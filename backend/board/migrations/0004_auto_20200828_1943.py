# Generated by Django 3.1 on 2020-08-28 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200827_1847'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reply',
            unique_together={('post', 'reply_order')},
        ),
    ]
