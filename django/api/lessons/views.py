from django.http import JsonResponse
from django.shortcuts import render

# splice
def sequences(request):
    a = [1, 2, 3]
    b = a[0:2]
    return JsonResponse(b, safe=False)

# tuples
def tuples(request):
    a = (1, 2, "3")
    b = a[0:2]
    c = a[0:3]
    return JsonResponse((b, c), safe=False)
  
# ranges
def ranges(request):
    a = range(0, 30, 6)
    b = 7 in a
    c = 12 in a
    return JsonResponse((list(a), b, c, a.index(6)), safe=False)