from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from pathlib import Path


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.title()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name.title()


class Institution(models.Model):
    name = models.CharField(max_length=50)
    place = models.ManyToManyField(Place, default="")
    url = models.URLField()

    def __str__(self):
        return self.name.title()


class Certification(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.name.title()


class Skill(models.Model):
    TYPE = (("IT", "IT Skill"), ("L", "Language Skill"))

    name = models.CharField(max_length=30)
    percent = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    category = models.CharField(max_length=2, choices=TYPE, default="IT")

    def __str__(self):
        return self.name.title()


class Experience(models.Model):
    TYPE = (("W", "Working"), ("E", "Education"))

    name = models.CharField(max_length=50)
    exp_type = models.CharField(max_length=1, choices=TYPE, default="W")
    start_time = models.DateField()
    end_time = models.DateField()
    institution = models.ManyToManyField(Institution)
    points = models.TextField(max_length=10000, default="")

    class Meta:
        ordering = ['-start_time']

    def __str__(self):
        return self.name.title()

    def get_points(self):
        if self.points:
            return self.points.split("\n")
        else:
            None


class Project(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)
    category = models.ManyToManyField(Category)
    date = models.DateField()
    url = models.URLField()
    desc = models.TextField()
    card_pic = models.ImageField(upload_to="projects/%Y/%m")
    pic1 = models.ImageField(upload_to="projects/%Y/%m")
    pic2 = models.ImageField(upload_to="projects/%Y/%m")
    pic3 = models.ImageField(upload_to="projects/%Y/%m")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name.title()


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, default="")
    institution = models.ManyToManyField(Institution)
    text = models.TextField(max_length=2000, default="")
    pic = models.ImageField(upload_to="testimonials/")

    def __str__(self):
        return self.name.title()


