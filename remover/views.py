from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import uuid
from rembg import remove
from rest_framework.views import APIView
from rest_framework.response import Response
import base64
import os


# Create your views here.
class HealthChecker(APIView):
    def get(self, request, format=None):
        return Response({"status": "OK."}, status=200)


class ImageRemover(APIView):

    def post(self, request, format=None):

        image = request.FILES["file"]
        imageId = f"{uuid.uuid4()}.png"

        with open(imageId, "wb") as f:
            for chunk in image.chunks():
                f.write(chunk)
        with open(imageId, "rb") as f:
            with open("new.png", "wb") as o:
                input = f.read()
                output = remove(input)
                o.write(output)
        with open("new.png", "rb") as f:
            responseData = f.read()
            responseData = base64.b64encode(responseData).decode("utf-8")
        os.remove(imageId)
        os.remove("new.png")
        return Response({"status": "success", "image": responseData})
