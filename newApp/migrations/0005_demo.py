# Generated by Django 4.0.3 on 2022-04-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0004_rename_is_admin_user_is_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
