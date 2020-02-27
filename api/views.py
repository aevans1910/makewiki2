from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from wiki.models import Page
from wiki.forms import PageForm
from api.serializers import PageSerializer

class PageList(APIView):
    def get(self, request):
        pages = Page.objects.all()[:5]
        data = PageSerializer(pages, many=True).data
        return Response(data)

class PageDetail(APIView):
    def get(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        data = PageSerializer(page).data
        return Response(data)

    def delete(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        page.delete()

class PageCreate(APIView):
    def post(self, request):
        form = PageForm(request.POST)
        data = PageSerializer(form).data
        return Response(data)

class PageUpdate(APIView):
    def put(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        form = PageForm(request.POST)
        data = PageSerializer(form).data
        return Response(data)
