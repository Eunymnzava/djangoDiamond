from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Donor(models.Model):
    donorID = models.AutoField(primary_key=True)
    username =models.CharField(max_length =25)
    password =models.CharField(max_length =25)
    email =models.EmailField(max_length =25) 
    phonenumber =models.CharField(max_length =25)
    

class Sponsor(models.Model):
    Sponsor_id = models.AutoField(primary_key=True)
    Name =models.CharField(max_length =25)
    Address =models.CharField(max_length =25)
    Email =models.EmailField(max_length =25) 
    Phone_number =models.CharField(max_length =25)
    


class Campaign(models.Model):
    CamID = models.AutoField(primary_key=True)
    Name =models.CharField(max_length =25)
    Description =models.CharField(max_length =500)
    Start_date =models.DateField()
    End_date =models.DateField() 
    Goal_amount =models.IntegerField( null=False, blank= False, default=0)
    Balance_amount = models.IntegerField(null=False, blank=False, default=0)
    Sponsor_id = models.ForeignKey (Sponsor, on_delete = models.CASCADE)


class Organization(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME =models.CharField(max_length =25)
    ADDRESS =models.CharField(max_length =25)
    donorID = models.ForeignKey (Donor, on_delete = models.CASCADE)



class paymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=25)


class Textmessage(models.Model):
    MesID = models.AutoField(primary_key=True)
    Timestamp =models.DateTimeField(auto_now_add=True)
    Context =models.CharField(max_length =25)
    CamID = models.ForeignKey (Campaign, on_delete = models.CASCADE)


class Transaction(models.Model):
    transid = models.AutoField(primary_key=True)
    amount =  models.IntegerField( null=False, blank= False, default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField (max_length = 25)
    donorID = models.ForeignKey(Donor, on_delete = models.CASCADE)
    id= models.ForeignKey(paymentMethod, on_delete = models.CASCADE) 






   
    
    

        