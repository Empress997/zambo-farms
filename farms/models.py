from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category Title")
    slug = models.SlugField(max_length=55, verbose_name="Category Slug")
    category_image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name="Category Image")

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Crop(models.Model):
    title = models.CharField(max_length=150, verbose_name="Crop Title")
    slug = models.SlugField(max_length=160, verbose_name="Crop Slug")
    category = models.ForeignKey(Category, verbose_name="Category", default=1 , on_delete=models.CASCADE)
    crop_description = models.TextField(verbose_name="Crop Description")
    crop_preparation = models.TextField(verbose_name="Crop Preparation")
    crop_planting = models.TextField(verbose_name="Crop Planting")
    crop_management = models.TextField(verbose_name="Pest and Disease Management")
    risk_dry_pest = models.TextField(verbose_name="Risk Assessment Pest")
    risk_dry_disease = models.TextField(verbose_name="Risk Assessment Disease")
    prevention_dry_pest = models.TextField(verbose_name="Control & Prevention Pest")
    prevention_dry_disease = models.TextField(verbose_name="Control & Prevention Disease")
    risk_rainy_pest = models.TextField(verbose_name="Risk Assessment Pest")
    risk_rainy_disease = models.TextField(verbose_name="Risk Assessment Disease")
    prevention_rainy_pest = models.TextField(verbose_name="Control & Prevention Pest")
    prevention_rainy_disease = models.TextField(verbose_name="Control & Prevention Disease")
    crop_image = models.ImageField(upload_to='Crop', blank=True, null=True, verbose_name="Crop Image")
    
    class Meta:
        verbose_name_plural = 'Crops'
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    fname = models.CharField(max_length=150, verbose_name="Contact Name", blank=False)
    email_address = models.EmailField(verbose_name="Email Address", blank=False)
    subject = models.CharField(max_length=100, verbose_name="Subject Message", blank=False)
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.subject

class NewsLetter(models.Model):
    email_address = models.EmailField(verbose_name="Email Address", blank=False)

    class Meta:
        verbose_name_plural = "News Letters"

    def __str__(self):
        return self.email_address

CATEGORY_CHOICES = (
    ('General','General'),
    ('Pag-asa','Pag-asa'),
    ('Department of Agriculture','Department of Agriculture')
)

class WhatsNew(models.Model):
    title = models.CharField(max_length=100, verbose_name="News Title", blank=False)
    background_image = models.ImageField(upload_to='News', blank=True, null=True, verbose_name="News Image")
    description = models.TextField(verbose_name="News Description")
    content = models.TextField(verbose_name="News Content")
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=100,
        default="General"
    )
    def __str__(self):
        return self.title
