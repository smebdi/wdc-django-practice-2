# Generated by Django 2.0 on 2018-08-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('album_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.CharField(default='rock', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='artistic_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
