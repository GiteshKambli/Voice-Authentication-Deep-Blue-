# Generated by Django 4.1.7 on 2023-04-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2', '0004_files_audio0_files_audio1_files_audio2_files_audio3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('phone', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]