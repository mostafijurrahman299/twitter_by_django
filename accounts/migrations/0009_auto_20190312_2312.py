# Generated by Django 2.1.2 on 2019-03-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190311_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True, null=True),
        ),
    ]