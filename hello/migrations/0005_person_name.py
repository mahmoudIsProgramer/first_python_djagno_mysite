# Generated by Django 2.0.7 on 2018-07-25 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20180725_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='mahmoud', max_length=100),
            preserve_default=False,
        ),
    ]