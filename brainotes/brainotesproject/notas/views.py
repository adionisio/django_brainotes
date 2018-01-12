# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notas.models import Nota,Usuario
from notas.serializers import NotaSerializer,UsuarioSerializer



# Create your views here.


"""
   Method to list all the existing notas
"""
@api_view(['GET', 'POST'])
def notas_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        notas = Nota.objects.all()
        serializer = NotaSerializer(notas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
    Method to list a nota
"""
@api_view(['GET', 'PUT', 'DELETE'])
def nota_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        nota = Nota.objects.get(pk=pk)
    except Nota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotaSerializer(nota)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NotaSerializer(nota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        nota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
   Method to list all existing users and add a new user
"""
@api_view(['GET', 'POST'])
def usuarios_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
   Method to list, modify or delete a user
"""
@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk, format=None):
   
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
   # Method to list all the notes of a user
   # @api_view(['GET'])
   # def notas_usuario(request, pk, format=None)
   # Implementar función que devuelva todas las notas de un usuario
"""
