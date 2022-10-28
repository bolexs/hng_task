from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(["GET"])
def home(request, *args, **kwargs):
  header = {"Access-Control-Allow-Origin":"*"}
  data = {
    "slackUsername":"bolex",
    "backend":True,
    "age": 21,
    "bio":"my name is bolu, i love taking challenges and trying to provide solutions to problems"
  }
  return JsonResponse(data,headers=header)