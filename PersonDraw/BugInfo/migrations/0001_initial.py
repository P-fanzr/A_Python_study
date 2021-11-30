# Generated by Django 3.2.7 on 2021-11-08 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PersonInfo', '0003_auto_20211102_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_bug', models.IntegerField(blank=True, max_length=50, verbose_name='功能缺陷')),
                ('flow_bug', models.IntegerField(blank=True, max_length=50, verbose_name='流程异常处理')),
                ('unique_bug', models.IntegerField(blank=True, max_length=50, verbose_name='参数唯一性约束')),
                ('beyond_bug', models.IntegerField(blank=True, max_length=50, verbose_name='参数范围约束')),
                ('need_bug', models.IntegerField(blank=True, max_length=50, verbose_name='必选参数约束')),
                ('interface_bug', models.IntegerField(blank=True, max_length=50, verbose_name='接口规范')),
                ('datatype_bug', models.IntegerField(blank=True, max_length=50, verbose_name='数据类型约束')),
                ('law_bug', models.IntegerField(blank=True, max_length=50, verbose_name='非法字符约束')),
                ('other_bug', models.IntegerField(blank=True, max_length=50, verbose_name='其他')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PersonInfo.person')),
            ],
            options={
                'verbose_name': 'bug类型',
                'verbose_name_plural': 'bug类型',
                'db_table': 'bug类型',
                'ordering': ('person',),
            },
        ),
    ]
