import json
from django.db.models.fields import related
from django.views import View #프론트엔드에게 보여주기위한 곳
from django.http import JsonResponse # 제이슨은 자바스크립트에서 파생이고 파이썬에서는 딕셔너리 형태로..  무조건 JsonResponse 아니다.
from.models import Actors
from.models import Movies

class ActorsView(View):
    def get(self,requset):
        act    = Actors.objects.all()
        result = [ ]
        for actors in act:
            movie_list=[]
            mov = actors.movies_set.all() # 역참조는 무조건 소문자로 한다.
            for movie in mov:
                movies_info = {
                'title':movie.title
                }
                movie_list.append(movies_info)
            
            actors_list ={
                'first-name': actors.first_name,
                'last_name':  actors.last_name,
                'title'    :  movie_list
            }
            
            result.append(actors_list)
        return JsonResponse({'result':result},status=200) #{'message':'Succes!'}  바디


class MoviesView(View):
    def get(self,requset):
        movies = Movies.objects.all()
        result = []
        for mov in movies:
            aclist=[]
            act = mov.actors.all()
            for actros in act:
                actors_list={
                    'first_name':actros.first_name,
                    'last_name':actros.last_name
                }
                aclist.append(actors_list)

            movies ={
                'movtitle':mov.title,
                'movrun':mov.running_time,
                'actors': aclist
            }
            result.append(movies)
        return JsonResponse({'result':result},status=200)

        


