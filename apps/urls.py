#!/usr/bin/env python
# encoding: utf-8
'''
@author: Luenci
@file: urls.py
@time: 1/10/2021 5:53 PM
'''

from django.conf.urls import url
from apps.views import *




urlpatterns = [
    url('^student/$', StudentListViewSet.as_view()),
    url('^student/<int:id>$', StudentListViewSet.as_view()),
    url('^student/course/',CourseListViewSet.as_view({'get': 'list','post': 'create'})),
    # url('^student/course/<int:id>$', CourseListViewSet.as_view()),

]


