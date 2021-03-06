# Generated by Django 2.0.13 on 2019-09-19 21:53

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djinn_contenttypes', '0001_initial'),
        ('djinn_events', '0002_auto_20190506_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_feed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_image', to='djinn_contenttypes.ImgAttachment'),
        ),
        migrations.AddField(
            model_name='event',
            name='image_feed_crop',
            field=image_cropping.fields.ImageRatioField('image_feed__image', '900x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image feed crop'),
        ),
    ]
