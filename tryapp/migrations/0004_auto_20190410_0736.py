# Generated by Django 2.0.13 on 2019-04-09 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tryapp', '0003_auto_20190409_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
