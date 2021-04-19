from typing import List

# from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

# from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Course, Student
from apps.serializer import CourseSerializer, StudentSerializer


class StudentListViewSet(APIView):
    permission_classes: List = [str]

    def get(self, request):
        students = Student.objects.all()
        students = StudentSerializer(students, many=True)
        return Response(students.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        if queryset.count() > 1:
            print("测试django doctor")
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        studentObjs = Student.objects.filter(id=id)
        serializer = StudentSerializer(studentObjs)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def post(self, request):
        data_dict = request.data
        serializer = StudentSerializer(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CourseListViewSet(viewsets.ModelViewSet):

    permission_classes: List[str] = []

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        courses = Course.objects.all()
        courses = self.get_serializer(courses, many=True)
        return Response(courses.data)

    def put(self, request, id):
        courseObjs = Course.objects.filter(id=id)
        serializer = StudentSerializer(courseObjs)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def post(self, request):
        data_dict = request.data
        serializer = StudentSerializer(data=data_dict)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
