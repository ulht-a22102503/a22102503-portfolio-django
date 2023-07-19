# Generated by Django 4.2.2 on 2023-07-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_tecnologia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='repo_link',
            new_name='source_code',
        ),
        migrations.AddField(
            model_name='projeto',
            name='website',
            field=models.URLField(default='https://www.github.com', max_length=500),
            preserve_default=False,
        ),
    ]
