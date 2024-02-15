from django.db import models
from django.contrib.auth.models import User
from customer.models  import customers
from product.models import products

# Create your models here.




class order(models.Model):
    
    LIVE=1
    DELETED=0
    DELETE_CHOICE=((LIVE,'live'),(DELETED,'deleted'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=(
        (ORDER_PROCCESSED,'order_processed'),
        (ORDER_DELIVERED,'order_delivered'),
        (ORDER_REJECTED,'order_rejected'),
    )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    owner=models.ForeignKey(customers,on_delete=models.SET_NULL,null=True,related_name='owner')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    
class ordereditem(models.Model):
    
    product=models.ForeignKey(products,on_delete=models.SET_NULL,null=True,related_name='product')
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name='itemowner')
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
        
    
    
