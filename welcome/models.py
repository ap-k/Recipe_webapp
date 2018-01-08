from django.db import models

class category(models.Model):
    cat_type = models.CharField(max_length=250)
    cat_name = models.CharField(max_length=500)
    cat_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.cat_name + ' - ' + self.cat_type



class ingredients(models.Model):
    Category = models.ForeignKey(category, on_delete=models.CASCADE)
    ing_name = models.CharField(max_length=250)

class main_course_1(models.Model):
    ingredient = models.CharField(max_length=250)
    recipe_name = models.CharField(default="abc",max_length=500)
    recipe_link = models.CharField(max_length=1000)

class main_course_2(models.Model):
    ingredient1 = models.CharField(max_length=250)
    ingredient2 = models.CharField(max_length=250)
    recipe_name = models.CharField(default="abc",max_length=500)
    recipe_link = models.CharField(max_length=1000)

class main_course_3(models.Model):
    ingredient1= models.CharField(max_length=250)
    ingredient2= models.CharField(max_length=250)
    ingredient3= models.CharField(max_length=250)
    recipe_name = models.CharField(default="abc",max_length=500)
    recipe_link= models.CharField(max_length=1000)

class main_course_4(models.Model):
    ingredient1= models.CharField(max_length=250)
    ingredient2= models.CharField(max_length=250)
    ingredient3= models.CharField(max_length=250)
    ingredient4= models.CharField(max_length=250)
    recipe_name = models.CharField(default="abc",max_length=500)
    recipe_link= models.CharField(max_length=1000)


class main_course_5(models.Model):
    ingredient1 = models.CharField(max_length=250)
    ingredient2 = models.CharField(max_length=250)
    ingredient3 = models.CharField(max_length=250)
    ingredient4 = models.CharField(max_length=250)
    ingredient5 = models.CharField(max_length=250)
    recipe_name= models.CharField(default="abc",max_length=500)
    recipe_link = models.CharField(max_length=1000)

class beverage_1(models.Model):
    ingredient1 = models.CharField(max_length=250)
    recipe_name = models.CharField(max_length=500)
    recipe_link = models.CharField(max_length=1000)

class beverage_2(models.Model):
    ingredient1 = models.CharField(max_length=250)
    ingredient2 = models.CharField(max_length=250)
    recipe_name = models.CharField(max_length=500)
    recipe_link = models.CharField(max_length=1000)

class beverage_3(models.Model):
    ingredient1 = models.CharField(max_length=250)
    ingredient2 = models.CharField(max_length=250)
    ingredient3 = models.CharField(max_length=250)
    recipe_name = models.CharField(max_length=500)
    recipe_link = models.CharField(max_length=1000)

class beverage_4(models.Model):
    ingredient1 = models.CharField(max_length=250)
    ingredient2 = models.CharField(max_length=250)
    ingredient3 = models.CharField(max_length=250)
    ingredient4 = models.CharField(max_length=250)
    recipe_name = models.CharField(max_length=500)
    recipe_link = models.CharField(max_length=1000)

class beverage_5(models.Model):
    ingredient1 = models.CharField(max_length=250)
    ingredient2 = models.CharField(max_length=250)
    ingredient3 = models.CharField(max_length=250)
    ingredient4 = models.CharField(max_length=250)
    ingredient5 = models.CharField(max_length=250)
    recipe_name = models.CharField(max_length=500)
    recipe_link = models.CharField(max_length=1000)

class Desserts_1(models.Model):
    ingredient1 = models.CharField(max_length=20)
    recipe_name = models.CharField(max_length=50)
    recipe_link = models.CharField(max_length=200)

class Desserts_2(models.Model):
    ingredient1 = models.CharField(max_length=20)
    ingredient2 = models.CharField(max_length=20)
    recipe_name = models.CharField(max_length=50)
    recipe_link = models.CharField(max_length=200)

class Desserts_3(models.Model):
    ingredient1 = models.CharField(max_length=20)
    ingredient2 = models.CharField(max_length=20)
    ingredient3 = models.CharField(max_length=20)
    recipe_name = models.CharField(max_length=50)
    recipe_link = models.CharField(max_length=200)

class Desserts_4(models.Model):
    ingredient1 = models.CharField(max_length=20)
    ingredient2 = models.CharField(max_length=20)
    ingredient3 = models.CharField(max_length=20)
    ingredient4 = models.CharField(max_length=20)
    recipe_name = models.CharField(max_length=50)
    recipe_link = models.CharField(max_length=200)

class Desserts_5(models.Model):
    ingredient1 = models.CharField(max_length=20)
    ingredient2 = models.CharField(max_length=20)
    ingredient3 = models.CharField(max_length=20)
    ingredient4 = models.CharField(max_length=20)
    ingredient5 = models.CharField(max_length=20)
    recipe_name = models.CharField(max_length=50)
    recipe_link = models.CharField(max_length=200)
