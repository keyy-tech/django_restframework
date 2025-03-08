from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET", "POST"])
def homepage(request: Request) -> Response:
    if request.method == "POST":
        data = request.data

        response = {
            "message": "Hello World",
            "data": data
        }

        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {
        "message": "Hello World"
    }
    return Response(data=response, status=status.HTTP_200_OK)

posts = [
    {
        "id": 1,
        "title": "Learning Django Rest Framework",
        "content": "This is me learning django rest framework"
    },
    {
        "id": 2,
        "title": "Story about Dog",
        "content": "The name of my pet is Belauh"
    },
    {
        "id": 3,
        "title": "Fun fact",
        "content": "I do love django"
    }
]

@api_view(['GET'])
def list_post(request: Request) -> Response:
    return Response(data=posts, status=status.HTTP_200_OK)

@api_view(['GET']) 
def list_post_detail(request: Request,id:int):
    post = posts[id]
    return Response(data=post,status=status.HTTP_200_OK)