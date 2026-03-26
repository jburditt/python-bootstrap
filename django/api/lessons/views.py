import copy, math, random
from django.http import JsonResponse
from django.shortcuts import render
from typing import TypeVar
from .model.colour import Colour

NumberT = TypeVar('NumberT', int, float)

class LessonViews:       
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

    # language reference
    def language_reference(request):
        
        result = {
            "string-formatting": "String formatting e.g. {0} and {1}".format("first", "second"),
        }
        # hash set and deep copy
        a = set([1, 2, 3, 3])
        b = copy.deepcopy(a)
        b.add(4)
        result.update({"a": list(a)})
        result.update({"b": list(b)})
        # enum
        result.update({"Colour.RED.name": Colour.RED.name})        
        # math
        result.update({"Math ceil": math.ceil(1.2)}) 
        # random
        result.update({"Math random": random.random()})
        return JsonResponse(result)
    
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Before execution")
            result = func(*args, **kwargs)
            print("After execution")
            return result
        return wrapper
    
    @staticmethod
    @my_decorator
    def decorated_function():
        print("Inside the decorated function")
        
    # generic function
    @staticmethod
    def add(a: NumberT, b: NumberT) -> NumberT:
        return a + b


LessonViews.decorated_function()
print(f"1 + 2 = {LessonViews.add(1, 2)}")
print(f"1.5 + 2.4 = {LessonViews.add(1.5, 2.4)}")
