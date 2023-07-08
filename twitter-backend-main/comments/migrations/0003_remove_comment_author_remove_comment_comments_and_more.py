# Generated by Django 4.1.4 on 2023-02-25 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0003_rename_type_meta_content_type'),
        ('comments', '0002_rename_comment_comment_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes_count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='posted_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='tweet',
        ),
        migrations.AddField(
            model_name='comment',
            name='meta',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='meta.meta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='meta.meta'),
            preserve_default=False,
        ),
    ]