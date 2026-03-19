from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view  # decorator is used to modify a function

# Create your views here.
def home(request):
    return HttpResponse("Welcome to API Home")

@api_view(['GET'])
def emplist(request):
    records=Employee.objects.all()
    serializer=EmployeeSerializer(records,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def empdetails(request,pk):
    try:
        record=Employee.objects.get(id=pk)
        serializer=EmployeeSerializer(record)
        return Response(serializer.data)
    except Exception as e:
        return HttpResponse("Employee not found")

@api_view(['POST'])
def empcreate(request):
    # print("data:",request.data)
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data Received and saved')
    else:
        return Response('Data not Valid/Received')

        
        


