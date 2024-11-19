from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='news/')
    reading_time = models.DurationField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while News.objects.filter(slug=slug).exists():
                slug = base_slug + str(count)
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Content(models.Model):
    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.subject}"


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
