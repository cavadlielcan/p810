from django.db import models

# from django.utils.translation import gettext_lazy as

class Blog(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to="blogs", null=True, blank=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "core.Author", related_name="blogs", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"
        ordering = ("title",)


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f" {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"
