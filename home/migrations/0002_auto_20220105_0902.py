# Generated by Django 2.2.12 on 2022-01-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(),
        ),
    ]