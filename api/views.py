from rest_framework import generics 
from .serializers import StringCalculatorSerializer
from .models import StringCalculator 

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    queryset = StringCalculator.objects.all()
    serializer_class = StringCalculatorSerializer

    def perform_create(self, serializer):
        serializer.save(strRes = add(serializer.validated_data['strReq']))

    def add(self, strParam): 
        p1 , p2 = strParam.split()
        result = int(p1) + int(p2) 
        return result

    