# Generated by Django 3.0.3 on 2020-03-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0006_auto_20200304_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='e_to',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='n_to',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='s_to',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='w_to',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
