# Generated by Django 4.1.4 on 2023-02-25 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meta', '0003_rename_type_meta_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReTweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refers', to='meta.meta')),
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meta.meta')),
            ],
        ),
    ]