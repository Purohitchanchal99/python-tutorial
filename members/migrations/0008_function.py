# Generated by Django 4.2.3 on 2023-11-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_oops'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=555)),
            ],
        ),
    ]
