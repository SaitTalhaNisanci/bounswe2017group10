# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 20:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('atlas', '0010_cultural_heritage_place_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorite_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='cultural_heritage',
            name='favorited_amount',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='favorite_items',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atlas.Cultural_Heritage'),
        ),
        migrations.AddField(
            model_name='favorite_items',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
