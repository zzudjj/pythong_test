# Generated by Django 5.0.7 on 2024-08-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_alter_contain_last_site_alter_contain_next_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.IntegerField()),
                ('line_id', models.IntegerField()),
                ('last_site_id', models.IntegerField()),
                ('next_site_id', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'line_view',
                'managed': False,
            },
        ),
    ]
