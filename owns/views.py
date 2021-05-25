import json
from django.views import View #프론트엔드에게 보여주기위한 곳
from django.http import JsonResponse # 제이슨은 자바스크립트에서 파생이고 파이썬에서는 딕셔너리 형태로..
from.models import Owners
from.models import Dogs
class OwnsListView(View):  
    def get(self, requst):
        own=Owners.objects.all()
        
        result = []
        for carname in own:
            result.append(carname.name)
        
        return JsonResponse({'result':result},status=200) #{'message':'Succes!'}  바디


    def post(self,request):#프론트엔드 에서 받아온 정보를 까봐야한다. 제이슨바디에 담아서 보내준다.
        data =json.loads(request.body)
        Owners.objects.create(name=data['name'],age=['age'],email=data['email'])
         
        return JsonResponse({'message':'SUCCESS!'},status=201) #{'message':'Succes!'}  바디


class DogsListView(View):
    def get(self,requset):
        dog =Dogs.objects.all()

    
        result = []
        for dogsname in dog:
             result.append(dogsname.name)
        return JsonResponse({'result':result},status=200)
        
    def post(self,request):#프론트엔드 에서 받아온 정보를 까봐야한다. 제이슨바디에 담아서 보내준다.
        data =json.loads(request.body)
        sk = Owners.objects.get(name=data['owners'])
        Dogs.objects.create(name=data['name'],age=data['age'], owners=sk)
        return JsonResponse({'message':'SUCCESS!'},status=200) #{'message':'Succes!'}  바디








        
