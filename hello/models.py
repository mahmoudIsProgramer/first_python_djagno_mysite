from django.db import models

# Create your models here.
class Person(models.Model):
    f_name = models.CharField(max_length=100, blank = "false")
    m_name = models.CharField(max_length=100, blank = "true" )
    l_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    

    
