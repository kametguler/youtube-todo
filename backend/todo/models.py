from django.db import models


class TodoModel(models.Model):
    class Meta:
        verbose_name = "Yapılacak"
        verbose_name_plural = "Yapılacaklar"

    name = models.CharField(max_length=255, verbose_name="İsim")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Güncelleşirme Tarihi"
    )
    is_done = models.BooleanField(default=False, verbose_name="Bitti mi ?")

    def __str__(self):
        return self.name
