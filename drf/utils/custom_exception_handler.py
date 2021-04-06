#!/usr/bin/env python
# encoding: utf-8
'''
@author: Luenci
@file: custom_exception_handler.py
@time: 3/23/2021 10:19 PM
'''
from rest_framework.views import exception_handler

def all_exception_handler(exc, context):
    """自定义异常类.

    :param exc:
    :param context:
    :return:
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response