from rest_framework.views import APIView
from .serializers import * 
from .models import *
from rest_framework.status import *
from django.http import JsonResponse

# Create your views here.
class CreateReminderView(APIView):
    def post(self, request):
        response = {"status": "success", "errorcode": "",
                    "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try:
            data = request.data
            serializer = ReminderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response['status'] = 'success'
                response["httpstatus"] = HTTP_201_CREATED
                response['result'] = serializer.data
            else:
                response['status'] = 'error'
                response["httpstatus"] = HTTP_400_BAD_REQUEST
                response['result'] = serializer._errors
                
        except Exception as e:
            response['status'] = 'error'
            response['errorcode'] = 500
            response['reason'] = str(e)
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
            
        return JsonResponse(response, status=response.get("httpstatus"))
        
        