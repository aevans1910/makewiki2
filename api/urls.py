from django.urls import path

from api.views import PageList, PageDetail, PageCreate

urlpatterns = [
    path('pages/', PageList.as_view(), name='pages_list'),
    path('pages/new/', PageCreate.as_view, name='page_new'),
    path('pages/<int:pk>/', PageDetail.as_view(), name='page_detail'),
]