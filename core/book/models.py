from django.db import models

# Create your models here.





class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(("Image Category"), upload_to='uploads/category/', blank=True, null=True)
    description = models.TextField(max_length=200, blank=True)

    
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})


class Books(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20, blank=True)
    cover = models.ImageField(("Book Cover"), upload_to='uploads/books/', blank=True, null=True)
    description = models.TextField(max_length=200, blank=True)
    audio_link = models.URLField(("Audio Link"), max_length=200, blank=True)
    rate = models.PositiveIntegerField(("Rate"), default=1, blank=True)
    cats = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE, blank=True)


    # price = models.DecimalField(max_digits=5, decimal_places=2)
    publish_date = models.DateField()

    

    class Meta:
        verbose_name = ("Books")
        verbose_name_plural = ("Bookss")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Books_detail", kwargs={"pk": self.pk})
