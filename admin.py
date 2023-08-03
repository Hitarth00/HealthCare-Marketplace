from django.contrib import admin
from .models import login,state,area,city,product_category,product_subcategory,customer_detail,product_detail,product_stock_detail,product_wishlist,product_cart,product_order,feedback,card_detail,contact

# Register your models here.

class show_login(admin.ModelAdmin):
    list_display = ['u_email','u_password','u_phone','u_role','u_status']
admin.site.register(login,show_login)

class show_state(admin.ModelAdmin):
    list_display = ['state_name']
admin.site.register(state,show_state)

class show_city(admin.ModelAdmin):
    list_display = ['city_name','State_id']
admin.site.register(city,show_city)

class show_area(admin.ModelAdmin):
    list_display = ['area_name','City_id','State']
admin.site.register(area,show_area)

class show_customer_detail(admin.ModelAdmin):
    list_display = ['name','L_id','dob','Address','display_photo','Area_id','City','State_idd']
admin.site.register(customer_detail,show_customer_detail)

class show_product_category(admin.ModelAdmin):
    list_display = ['Product_category_name']
admin.site.register(product_category,show_product_category)

class show_product_subcategory(admin.ModelAdmin):
    list_display = ['Product_subcategory_name','Product_cat']
admin.site.register(product_subcategory,show_product_subcategory)

class show_product_detail(admin.ModelAdmin):
    list_display = ['Pro_name','Pro_cat','Pro_Subcat','display_photo2','Pro_description','Pro_price']
admin.site.register(product_detail,show_product_detail)

class show_product_stock_detail(admin.ModelAdmin):
    list_display = ['Pro_id','Quantity','Updated_time']
admin.site.register(product_stock_detail,show_product_stock_detail)

class show_product_wishlist(admin.ModelAdmin):
    list_display = ['Product_id','L_id','Date_time']
admin.site.register(product_wishlist,show_product_wishlist)

class show_product_cart(admin.ModelAdmin):
    list_display = ['Product_idd','L_idd','Product_name','Date_timee','Price','pro_quantity','Final_price','Order_id','Order_status']
admin.site.register(product_cart,show_product_cart)

class show_product_order(admin.ModelAdmin):
    list_display = ['Total_amount','L_iddd','Address','order_status','Payment_status','Date_time']
admin.site.register(product_order,show_product_order)

class show_feedback(admin.ModelAdmin):
    list_display = ['L_ID','Ratings','Comment']
admin.site.register(feedback,show_feedback)

class show_card_detail(admin.ModelAdmin):
    list_display = ['name','card_number','card_cvv','exp_date','card_balance']
admin.site.register(card_detail,show_card_detail)

class show_contact(admin.ModelAdmin):
    list_display = ['name','email','subject','phone','message']
admin.site.register(contact,show_contact)