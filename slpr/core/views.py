# coding: utf-8


from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import tempfile
import os
import json


class IndexAPIView(APIView):
    def post(self, request):
        if not request.FILES.get("file"):
            return JsonResponse({
                "error": "no file given"
            }, status=status.HTTP_400_BAD_REQUEST)

        request_file = request.FILES.get("file")
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, request_file.name), "wb") as f:
                f.write(request_file.read())
            content = os.popen("alpr -c br -j {}".format(
                os.path.join(tmpdirname, request_file.name)
            )).read()

        if not content:
            return JsonResponse({
                "error": "no license plate found"
            }, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(json.loads(content))
