# Generated by Django 2.2.2 on 2019-07-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0004_fanunbalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanunbalance',
            name='balance_grade',
            field=models.CharField(choices=[('1', '1'), ('2.5', '2.5'), ('6.3', '6.3')], default=2.5, max_length=10),
            preserve_default=False,
        ),
    ]