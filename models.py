from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

CHOICE=[
    ("1","ADMIN"),
    ("2","USER")
]
CHOICES=[
    ("1","ACTIVE"),
    ("2","INACTIVE")
]
STATUS=[
    ("1","PENDING"),
    ("2","CLOSED")
]
class login(models.Model):
    u_email=models.EmailField()
    u_password=models.CharField(max_length=20)
    u_phone=models.IntegerField()
    u_role=models.CharField(max_length=10, choices=CHOICE)
    u_status=models.CharField(max_length=10, choices=CHOICES)
    def __str__(self):
        return self.u_email

class state(models.Model):
    state_name=models.CharField(max_length=20)
    def __str__(self):
        return self.state_name

class city(models.Model):
    city_name=models.CharField(max_length=20)
    State_id=models.ForeignKey(state,on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name

class area(models.Model):
    area_name=models.CharField(max_length=20)
    City_id=models.ForeignKey(city,on_delete=models.CASCADE)
    State=models.ForeignKey(state,on_delete=models.CASCADE)
    def __str__(self):
        return self.area_name

class customer_detail(models.Model):
    name=models.CharField(max_length=30)
    L_id=models.ForeignKey(login,on_delete=models.CASCADE)
    dob=models.DateField()
    Address=models.TextField()
    dp=models.ImageField(upload_to='photos')
    Area_id=models.ForeignKey(area,on_delete=models.CASCADE)
    City=models.ForeignKey(city,on_delete=models.CASCADE)
    State_idd=models.ForeignKey(state,on_delete=models.CASCADE)
    def display_photo(self):
        return mark_safe("<img src='{}' width='100' />".format(self.dp.url))

class product_category(models.Model):
    Product_category_name=models.CharField(max_length=20)
    def __str__(self):
        return self.Product_category_name

class product_subcategory(models.Model):
    Product_subcategory_name=models.CharField(max_length=20)
    Product_cat=models.ForeignKey(product_category,on_delete=models.CASCADE)

    def __str__(self):
        return self.Product_subcategory_name

class product_detail(models.Model):
    Pro_name=models.CharField(max_length=20)
    Pro_cat=models.ForeignKey(product_category,on_delete=models.CASCADE)
    Pro_Subcat=models.ForeignKey(product_subcategory,on_delete=models.CASCADE)
    Pro_image=models.ImageField(upload_to='photos')
    Pro_description=models.TextField()
    Pro_price=models.IntegerField()
    def __str__(self):
        return self.Pro_name
    def display_photo2(self):
        return mark_safe("<img src='{}' width='100' />".format(self.Pro_image.url))


class product_stock_detail(models.Model):
    Pro_id=models.ForeignKey(product_detail,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Updated_time=models.TimeField()

class product_wishlist(models.Model):
    Product_id=models.ForeignKey(product_detail,on_delete=models.CASCADE)
    L_id=models.ForeignKey(login,on_delete=models.CASCADE)
    Date_time=models.DateTimeField()

class product_cart(models.Model):
    Product_idd=models.ForeignKey(product_detail,on_delete=models.CASCADE)
    L_idd = models.ForeignKey(login,on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=20)
    Date_timee=models.DateTimeField()
    Price=models.IntegerField()
    pro_quantity=models.IntegerField()
    Final_price=models.IntegerField()
    Order_id=models.IntegerField()
    Order_status=models.IntegerField()

class product_order(models.Model):
    Total_amount=models.IntegerField()
    L_iddd = models.ForeignKey(login,on_delete=models.CASCADE)
    Address=models.TextField()
    order_status=models.CharField(max_length=10, choices=STATUS)
    Payment_status=models.CharField(max_length=20)
    Date_time=models.DateTimeField()

class feedback(models.Model):
    L_ID = models.ForeignKey(login,on_delete=models.CASCADE)
    Ratings = models.CharField(max_length=20)
    Comment = models.TextField()

class card_detail(models.Model):
    name=models.CharField(max_length=10)
    card_number=models.IntegerField()
    card_cvv=models.IntegerField()
    exp_date=models.DateField()
    card_balance=models.IntegerField()

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=20)
    phone=models.IntegerField()
    message=models.TextField()






