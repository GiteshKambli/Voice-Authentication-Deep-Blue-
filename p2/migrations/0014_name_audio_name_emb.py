# Generated by Django 4.1.7 on 2023-04-05 13:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2', '0013_alter_files_embeddings0_alter_files_embeddings1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='audio',
            field=models.FileField(default=123, upload_to='tp/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='name',
            name='emb',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
    ]