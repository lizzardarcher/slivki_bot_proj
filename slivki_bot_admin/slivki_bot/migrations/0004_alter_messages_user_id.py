# Generated by Django 3.2.6 on 2021-08-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slivki_bot', '0003_messages_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
