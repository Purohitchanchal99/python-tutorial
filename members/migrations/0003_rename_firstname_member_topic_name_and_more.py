# Generated by Django 4.2.3 on 2023-11-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='firstname',
            new_name='topic_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='joined_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone',
        ),
        migrations.AddField(
            model_name='member',
            name='description',
            field=models.CharField(default='Your default description here', max_length=255),
        ),
    ]