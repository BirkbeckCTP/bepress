from django.db import models
from django.utils import timezone


class ImportedArticle(models.Model):
    dump_name = models.CharField(max_length=255, blank=True, null=True)
    article = models.ForeignKey('submission.Article', blank=True, null=True)
    bepress_id = models.BigIntegerField()
    journal = models.ForeignKey('journal.Journal')
    started = models.DateTimeField(default=timezone.now)


    class Meta:
        unique_together = (
                ("article", "bepress_id", "dump_name"),
        )

class ImportedArticleAuthor(models.Model):
    article = models.ForeignKey(
            "submission.Article", related_name="bepress_importedarticleauthor")
    author = models.ForeignKey(
            "core.Account", related_name="bepress_importedarticleauthor")

    class Meta:
        unique_together = (("article", "author"),)

