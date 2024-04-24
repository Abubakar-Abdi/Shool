from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
)
from .forms import StudentForm 



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Student created successfully'}, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
