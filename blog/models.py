from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    profession = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Info(TimeStampedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.name


class About(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    info = models.ManyToManyField(Info)

    def __str__(self):
        return self.title


class Clients(TimeStampedModel):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Comments(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
