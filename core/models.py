from django.db import models
from PIL import Image



class Stack(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)
    #github =
    #demo =

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


        #open file for editing 
        img = Image.open(self.image.path)

        # Determine the new size and the box to crop
        min_dimension = min(img.width, img.height)
        left = (img.width - min_dimension) / 2
        top = (img.height - min_dimension) / 2
        right = (img.width + min_dimension) / 2
        bottom = (img.height + min_dimension) / 2

        # Crop the image to be a square
        img = img.crop((left, top, right, bottom))
        
        # Optionally, you can resize the image to a specific size
        img = img.resize((min_dimension, min_dimension), Image.Resampling.LANCZOS)
        
        # Save the modified image
        img.save(self.image.path)

    def __str__(self):
        return self.title

