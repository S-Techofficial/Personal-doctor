# Generated by Django 3.0.3 on 2020-03-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaldoc', '0008_auto_20200305_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='problem',
        ),
        migrations.AddField(
            model_name='patients',
            name='Problem',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='solutions',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
