from django.db import models

# A simple User model to store the sign-up information
class Signup(models.Model):
    user = models.CharField(max_length=30, unique=True)
    pasw = models.CharField(max_length=255)  # Use hashed password
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.user
    
class Cakes(models.Model):
        cakes_image = models.ImageField(upload_to='cakes/')
        title=models.CharField(max_length=50)
        amount=models.DecimalField(max_digits=10,decimal_places=2)

class Cookies(models.Model):
        cookies_image = models.ImageField(upload_to='cookies/')
        title=models.CharField(max_length=50)
        amount=models.DecimalField(max_digits=10,decimal_places=2)

class Chaats(models.Model):
        chaats_image = models.ImageField(upload_to='chaats/')
        title=models.CharField(max_length=50)
        amount=models.DecimalField(max_digits=10,decimal_places=2)

class Order(models.Model):
    product_name = models.CharField(max_length=100)
    quantity= models.IntegerField(default=1)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    address = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} ordered by {self.customer_name}"
    
class Feedback(models.Model):
      name=models.CharField(max_length=100)
      email=models.EmailField(max_length=100)
      message=models.TextField(default='')
      
      def __str__(self):
        return f"Message from {self.name}"









