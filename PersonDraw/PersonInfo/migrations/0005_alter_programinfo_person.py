# Generated by Django 3.2.7 on 2021-11-26 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PersonInfo', '0004_auto_20211125_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programinfo',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_id', to='PersonInfo.person'),
        ),
    ]