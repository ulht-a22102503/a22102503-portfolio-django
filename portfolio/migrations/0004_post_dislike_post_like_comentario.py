# Generated by Django 4.2.2 on 2023-07-19 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=20)),
                ('texto', models.CharField(max_length=2000)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.post')),
            ],
        ),
    ]