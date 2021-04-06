#!/usr/bin/env python
# encoding: utf-8
"""
@author: Luenci
@file: serializer.py
@time: 1/10/2021 6:35 PM
"""

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.models import Student, Course


class StudentSerializer(serializers.Serializer):
    """
    学生类序列化器.
    """

    name = serializers.CharField(label="姓名", max_length=30)
    age = serializers.IntegerField(label="年龄")
    gender = serializers.ChoiceField(
        choices=(('male', '男'), ('female', '女')),
        default='male'
    )

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def validate_gender(self, gender):
        pass



class CourseSerializer(ModelSerializer):
    """
    课程类序列化器.
    """

    class Meta:
        model = Course
        fields = "__all__"


    def validate_scores(self, scores):
        if scores < 0 or scores > 100:
            raise serializers.ValidationError("scores不能小于0或大于100！")
        else:
            return int(scores)
