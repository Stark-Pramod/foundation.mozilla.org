# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailpages', '0007_auto_20180404_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'image', 'hr'])), ('image_text', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image on the left'), ('right', 'Image on the right')]))))), ('image', wagtail.images.blocks.ImageChooserBlock()), ('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False))))), ('figuregrid', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('video', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please make sure this is a proper embed URL, or your video will not show up on the page.')), ('height', wagtail.core.blocks.IntegerBlock(default=450))))), ('iframe', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('height', wagtail.core.blocks.IntegerBlock(default=450))))), ('linkbutton', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button'), ('btn-success', 'Success button'), ('btn-info', 'Info button'), ('btn-warning', 'Warning button'), ('btn-error', 'Error button'), ('btn-ghost', 'Ghost button')])), ('outline', wagtail.core.blocks.BooleanBlock(default=False, required=False))))), ('spacer', wagtail.core.blocks.StructBlock((('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')])),)))))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
