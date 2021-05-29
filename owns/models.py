from django.db import models

class Owners(models.Model):
    name  = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age   = models.IntegerField()
    
    
    class Meta:
        db_table = 'owners'



class Dogs(models.Model):
    owners  = models.ForeignKey(Owners,on_delete=models.CASCADE)
    name    = models.CharField(max_length=45)
    age     = models.IntegerField()
    
    class Meta:
        db_table = 'dogs'#테이블명



 