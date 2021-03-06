# Generated by Django 3.0.2 on 2020-02-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200213_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('country', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.AddField(
            model_name='book',
            name='people',
            field=models.ManyToManyField(to='app.Person'),
        ),
    ]
