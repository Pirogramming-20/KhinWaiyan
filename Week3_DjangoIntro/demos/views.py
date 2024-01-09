from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
#   return HttpResponse('장고세션 어려워요')
  return render(request, 'demos/index.html')

def calculator(request):
  # return HttpResponse('계산기 기능 구현 시작입니다. 이게 맞나요?')
  
  # 1. 데이터 확인
  num1 = request.GET.get('num1')
  num2 = request.GET.get('num2')
  operators = request.GET.get('operators')
  
  # 2. 계산
  if operators == '+':
    result = int(num1) + int(num2)
  elif operators == '-':
    result = int(num1) - int(num2)
  elif operators == '*':
    result = int(num1) * int(num2)
  elif operators == '/':
    result = int(num1) / int(num2)
  else:
    result = 0
    
  # 3. 응답
  return render(request, 'demos/calculator.html', {'result': result})