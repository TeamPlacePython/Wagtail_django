from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    max_count = 1

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255,
        help_text="Write an introduction for the site",
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    summary = models.TextField(blank=True, max_length=500)
    cta_text = models.CharField(max_length=50, blank=True)
    cta_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    cta_url = models.URLField(blank=True)

    my_story_title = models.CharField(
        max_length=40, blank=True, default="My Story"
    )
    my_story_content = models.TextField(blank=True, max_length=800)

    content_panels = Page.content_panels + [
        FieldPanel("author_image"),
        FieldPanel("summary"),
        FieldPanel("cta_text"),
        FieldPanel("cta_page"),
        FieldPanel("cta_url"),
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
                FieldPanel("my_story_title"),
                FieldPanel("my_story_content"),
            ],
            heading="My Story",
        ),
        FieldPanel("body"),
    ]

    @property
    def cta_link(self):
        if self.cta_page:
            return self.cta_page.url
        elif self.cta_url:
            return self.cta_url
        return None

    @property
    def button_text(self):
        return self.cta_text or "Read More"
