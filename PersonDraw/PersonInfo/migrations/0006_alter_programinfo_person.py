# Generated by Django 3.2.7 on 2021-11-26 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PersonInfo', '0005_alter_programinfo_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programinfo',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_item', to='PersonInfo.person'),
        ),
    ]
