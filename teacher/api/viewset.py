from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import status
from teacher.models import *
from .serializer import *

class TeacherViewSet(ModelViewSet):
    model = Teacher
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    http_method_names = ['get', 'post','patch','delete']
    def list(self,request,*args, **kwargs):
        print("salammmm")
        print(self.request.query_params)
        print(Teacher.objects.filter(**self.request.query_params),'dataa')
        queryset = Teacher.objects.all()
        serializer = TeacherSerializer(queryset, many=True)
        #self.request.query_params.get('order_by', None)
        #print(request.body)
        return Response(serializer.data)
        
class FenViewSet(ModelViewSet):
    model = Fen
    serializer_class = FenSerializer
    queryset = Fen.objects.all()
    http_method_names = ['get', 'post','patch','delete']
 
class IxtisasViewSet(ModelViewSet):
    model = Ixtisas
    serializer_class = IxtisasSerializer
    queryset = Ixtisas.objects.all()
    http_method_names = ['get', 'post','patch','delete']
