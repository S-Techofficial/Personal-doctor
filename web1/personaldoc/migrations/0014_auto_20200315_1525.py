# Generated by Django 3.0.3 on 2020-03-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaldoc', '0013_auto_20200312_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='tags',
        ),
        migrations.AddField(
            model_name='doctors',
            name='specialist',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
