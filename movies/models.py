from django.db import models

class Actors(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateField()


    class Meta:
        db_table = 'actors'
#============================
   # 중간테이블 Actors_Movies
#===========================
class Movies(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actors        = models.ManyToManyField(Actors)
    class Meta:
        db_table = 'movies'



