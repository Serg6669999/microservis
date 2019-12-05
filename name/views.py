from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import random


@csrf_exempt
def response(request):
    if request.method == 'POST':
        data = request.body
        print('request = ', data)
        data_dict = json.loads(data)
        number_1 = int(data_dict['number_1'])
        number_2 = int(data_dict['number_2'])
        print('data_dict = ', data_dict)
        print('1 = ', number_1)
        print('2 = ', number_2)
        print(' = ', number_2+number_1)
        random_number = random.randint(number_1, number_2)
        response_dict = {'number': random_number}
        print(response_dict)
        return JsonResponse(response_dict)
