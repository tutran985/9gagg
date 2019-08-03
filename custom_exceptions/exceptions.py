
from __future__ import unicode_literals
from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _

def custom_exception_handler(exc, context):

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    # if response is not None:
    #     response.data['status_code'] = response.status_code

    return response