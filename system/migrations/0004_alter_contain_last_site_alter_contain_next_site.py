# Generated by Django 5.0.7 on 2024-08-09 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_line_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contain',
            name='last_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_site', to='system.site', verbose_name='上一站点编号'),
        ),
        migrations.AlterField(
            model_name='contain',
            name='next_site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_site', to='system.site', verbose_name='下一站点编号'),
        ),
    ]
