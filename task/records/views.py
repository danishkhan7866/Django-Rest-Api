from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Studentlist(ListAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer

class StudentlistCreate(ListCreateAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer

class StudentRetrieveupdateDestroy(RetrieveUpdateDestroyAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
