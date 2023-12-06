from django.http import JsonResponse
from .models import Films
from .serializers import FilmSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# create all the endpoints that you can acces your data from
# 1)dostat vsetky filmy 2)serialize ich 3)return json

#funkcia ktora dostane get request a zobrazi to cize read
@api_view(['GET', 'POST'])
def Films_list(request):
    if request.method == 'GET':
        films = Films.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def films_detail(request, id):
    try:
        film=Films.objects.get(pk=id)
    except Films.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=FilmSerializer(film)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
