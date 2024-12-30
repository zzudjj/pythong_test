# Generated by Django 5.0.7 on 2024-08-23 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0014_alter_complaint_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='违章编号')),
                ('title', models.CharField(max_length=90, verbose_name='违章标题')),
                ('text', models.TextField(verbose_name='违章内容')),
                ('status', models.IntegerField(choices=[(0, '未处理'), (1, '已通过'), (2, '未通过')], default=0, verbose_name='处理状态')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.driver', verbose_name='被投诉司机工号')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.manager', verbose_name='处理人员')),
                ('passenger_tel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.passenger', verbose_name='投诉人电话')),
            ],
            options={
                'db_table': 'violation',
            },
        ),
    ]
