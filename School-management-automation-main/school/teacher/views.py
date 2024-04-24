from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(['GET'])
@permission_classes([IsAuthenticated & IsAdminUser])  # Adjust permissions as needed
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        name_search = request.GET.get('name', None)
        if name_search:
            teachers = teachers.filter(name__icontains=name_search)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
