from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Author(models.Model):
	CHOICES = (
		('Junior','Junior'),
		('Middle','Middle'),
		('Master','Master'),
		('Senior','Senior'),
		)
	name = models.CharField(max_length=50)
	portrait = models.ImageField(upload_to='portraits/')
	birthday = models.DateField(auto_now_add=None)
	website = models.CharField(max_length=200)
	phone = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	degree = models.CharField(max_length=100, choices=CHOICES)
	phEmailone = models.EmailField()
	freelance = models.BooleanField()
	desc = RichTextField()
	class Meta:
		verbose_name = 'Author'

	def __str__(self):
		return f"Author - {self.name}"

class Facts_Scils(models.Model):
	html = models.PositiveIntegerField()
	css = models.PositiveIntegerField()
	bootstrap = models.PositiveIntegerField()
	cpp = models.PositiveIntegerField()
	django = models.PositiveIntegerField()
	photoshop = models.PositiveIntegerField()
	
	class Meta:
		verbose_name = 'Fact and Scil'

	def __str__(self):
		return f"Fact and Scil"
class Resume(models.Model):
	CHOICES = (
		('Sumary','Sumary'),
		('Education','Education'),
		('Professional_Experience','Professional_Experience'),
		)
	theme = models.CharField(max_length=50,choices=CHOICES,null=True)
	title = models.CharField(max_length=100, null=True)
	date = models.CharField(max_length=100, null=True)
	place = models.CharField(max_length=100, null=True)
	desc = RichTextField(null=True)

	class Meta:
		verbose_name = 'Resume'

	def __str__(self):
		return f"Resume - {self.title}"

class Experiences(models.Model):
	experiences = models.ForeignKey(Resume, on_delete=models.CASCADE)
	text = RichTextField()

	class Meta:
		verbose_name = 'Experience'
		verbose_name_plural = 'Experiences'

class Portfolio(models.Model):
	category = models.CharField(max_length=50) 
	client = models.CharField(max_length=50)
	project_date = models.DateField(auto_now_add=False)
	project_url = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	poster = models.ImageField(upload_to='portfolio_posters/', null=True)
	slug = models.SlugField('*', unique=True,null=True)
	desc = RichTextField()

	class Meta:
		verbose_name = 'Portfolio'
		verbose_name_plural = 'Portfolios'

	def get_portfolio(self):
		return reverse('about_me:portfolio_detail', kwargs={'portfolio_slug':self.slug})

	def __str__(self):
		return f"Portfolio - {self.title}"

class Portfolio_Images(models.Model):
	experiences = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='portfolio_images/')

	class Meta:
		verbose_name = 'Portfolio_Image'
		verbose_name_plural = 'Portfolio_Images'

class Testimonials(models.Model):
	name = models.CharField(max_length=50)
	job = models.CharField(max_length=50)
	poster = models.ImageField(upload_to='testimonials_poster/')
	desc = models.TextField()

	class Meta:
		verbose_name = 'Testimonial'
		verbose_name_plural = 'Testimonials'
		
	def __str__(self):
		return f"Testimonial - {self.name}"
class Contact(models.Model):
	name = models.CharField(max_length=50)
	email =  models.EmailField()
	subject = models.CharField(max_length=50)
	message = models.TextField()

	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return f"Message from - {self.name}"
	


