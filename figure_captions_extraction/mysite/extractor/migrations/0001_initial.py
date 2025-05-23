# Generated by Django 5.2.1 on 2025-05-19 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmc_id', models.CharField(max_length=50, unique=True)),
                ('title', models.TextField(blank=True)),
                ('abstract', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.TextField()),
                ('figure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='extractor.figure')),
            ],
        ),
        migrations.AddField(
            model_name='figure',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='figures', to='extractor.paper'),
        ),
    ]
