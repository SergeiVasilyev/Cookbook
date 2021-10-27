from django.db import models
# from autoslug import AutoSlugField

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"ReseptiList: {self.id} | {self.cat_name}"
    
class Ingridient(models.Model):
    ing_name = models.CharField(max_length=200)

    def __str__(self):
        return f"ReseptiList: {self.id} | {self.ing_name}"
    
class Resepti(models.Model):
    headline = models.CharField(max_length=300)
    body_text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    # slug = AutoSlugField(populate_from='headline')
    categoryFK = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True) #SET_DEFAULT , to_field='name'
    ingridientFK = models.ForeignKey(Ingridient, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"ReseptiList: {self.id} | {self.headline}"
    