from django.db import models
from django.utils import timezone
try:
    from plugins import books
except ImportError:
    books = None


class ImportedArticle(models.Model):
    dump_name = models.CharField(max_length=255, blank=True, null=True)
    article = models.ForeignKey(
        'submission.Article', blank=True, null=True,
        on_delete=models.CASCADE,
    )
    bepress_id = models.BigIntegerField()
    journal = models.ForeignKey(
        'journal.Journal',
        on_delete=models.CASCADE,
    )
    started = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (
                ("article", "bepress_id", "dump_name"),
        )


class ImportedArticleAuthor(models.Model):
    article = models.ForeignKey(
        "submission.Article", related_name="bepress_importedarticleauthor",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        "core.Account", related_name="bepress_importedarticleauthor",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (("article", "author"),)


if books:
    class ImportedChapter(models.Model):
        book = models.ForeignKey(
            "books.Book",
            null=True, blank=True,
            on_delete=models.SET_NULL,
        )
        chapter = models.ForeignKey(
            "books.Chapter",
            null=True, blank=True,
            on_delete=models.SET_NULL,
        )
        bepress_id = models.PositiveIntegerField()

        class Meta:
            unique_together = ("book", "chapter", "bepress_id")
