from rest_framework.decorators import api_view
from rest_framework.response import Response
from loans.loanoops import *

@api_view(['POST'])
def loancalc(request):
    input_data=request.data
    obj=Loan(input_data)
    data=Loan.amortizationtab(obj) 
    return Response(data)

# Create your views here.
