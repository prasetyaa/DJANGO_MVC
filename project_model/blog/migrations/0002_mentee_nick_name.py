# Generated by Django 2.1.5 on 2019-02-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='nick_name',
            field=models.TextField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
