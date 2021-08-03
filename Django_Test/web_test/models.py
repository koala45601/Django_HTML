from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Stock_Me(models.Model):
    Stock_name = models.CharField(max_length=100)
    #Stock_ID = models.AutoField(primary_key="True")
    Stock_ID = models.IntegerField(default=0)
    Category_select = (('Meet','Meet'),
    ('Farm','Farm'),
    ('Tools','Tools'),
    ('Book','Book'))
    category=models.CharField(max_length=200, choices=Category_select, default='Meet')
    socrce= models.IntegerField(default=0)
    Stock_remark = models.CharField(max_length=200,blank=True,null=True)
    img = models.ImageField(upload_to='stock_img',blank=True,null=True)

    def __str__(self):
        return self.Stock_name + '-' + self.category

class Local_stock(models.Model):
    provids1 = (('Bangkok','Bangkok'),
                   ('ChiangMai','ChiangMai'),
                   ('ChiangRai','ChiangRai'),
                   ('Kamphaeng','Kamphaeng'))
    provi= models.CharField(max_length=100, choices=provids1, default='Bangkok')
    Stock_name = models.CharField(max_length=200)
    Stock_ID = models.CharField(max_length=4)
    manager_name = models.CharField(max_length=100)
    branch_Tel = models.CharField(max_length=10)
    Stock_remark = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.Stock_ID + '-'+ self.Stock_name + '-'+ self.provi+'-'+self.manager_name+'-'+self.branch_Tel
        
class img_product(models.Model):
    Stock_name = models.OneToOneField(Stock_Me,on_delete=models.CASCADE)
    product_img = models.ImageField(default='default.png',upload_to='img_product',blank=True,null=True)

    def __str__(self):
        return f'{self.Stock_name.Stock_name} Profile'


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img_profile = models.ImageField(default='default.png',upload_to='img_profile',blank=True,null=True)
    usertype = models.CharField(max_length=100,null=True,blank=True,default='emp')

    def __str__(self):
        return f'{self.user.username} Profile'


class upload_document(models.Model):
    userlevel_list = (('Admin','Admin'),('customer','customer'))
    userlevel = models.CharField(max_length=50,choices=userlevel_list,       default='Admin')
    document_name = models.CharField(max_length=150)
    document_up = models.FileField(upload_to='alldoc',blank=True,null=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.document_name





