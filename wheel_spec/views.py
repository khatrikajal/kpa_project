
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

@api_view(['POST'])
def submit_wheel_spec(request):
    serializer = WheelSpecificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Wheel specification form submitted successfully.", "success": True}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_filtered_wheel_specs(request):
    formNumber = request.GET.get('formNumber')
    submittedBy = request.GET.get('submittedBy')
    submittedDate = request.GET.get('submittedDate')

    filters = {}
    if formNumber:
        filters['formNumber'] = formNumber
    if submittedBy:
        filters['submittedBy'] = submittedBy
    if submittedDate:
        filters['submittedDate'] = submittedDate

    specs = WheelSpecification.objects.filter(**filters)
    serializer = WheelSpecificationSerializer(specs, many=True)
    return Response({"data": serializer.data, "message": "Filtered wheel specification forms fetched successfully.", "success": True})

