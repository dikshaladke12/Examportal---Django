from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phoneNo = models.CharField(max_length =12,null=True)

class resetuuid(models.Model):
    UUID = models.UUIDField(unique=True)
    user = models.ForeignKey(to = User, on_delete= models.CASCADE)
    expiry = models.DateTimeField()   

class UserTable(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.f_name
 
choices = (
        ('is_mcq','is_mcq'),
        ('is_theory','is_theory')        
    ) 
  
class Question(models.Model):
    
   
    question = models.CharField(max_length=100)
    q_type = models.CharField(max_length=50, choices=choices)
    
    def __str__(self):
        return self.question
    
class Options(models.Model):
    option = models.CharField(max_length=50)
    question = models.ForeignKey(to = Question, on_delete = models.CASCADE)
    is_correct = models.BooleanField(default= False)
    
    def __str__(self):
        return self.option
    
    
class AnswerTable(models.Model):
    u_id = models.ForeignKey(to = UserTable , on_delete=models.SET_NULL, null=True)
    q_id = models.ForeignKey(to = Question , on_delete= models.CASCADE)
    o_id = models.ForeignKey(to = Options , on_delete= models.SET_NULL, null= True, blank=True)    
    ans = models.TextField(max_length= 100, null= True , blank=True) 