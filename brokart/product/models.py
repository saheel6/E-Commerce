from django.db import models

# Create your models here.



class products(models.Model):
    
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'live'),(DELETE,'delete'))
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='photos')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    