from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SampleView(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        response = {"message": "Valid response"}
        return Response(response, status=status.HTTP_200_OK)
