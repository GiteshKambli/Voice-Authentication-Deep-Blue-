# Generated by Django 4.1.7 on 2023-04-04 14:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2', '0007_remove_files_embeddings0_remove_files_embeddings1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='embeddings0',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings4',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings6',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings7',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings8',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='embeddings9',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=[2.2], size=None),
            preserve_default=False,
        ),
    ]
