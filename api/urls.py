from django.urls import path


from .views import TodoListAPIView

urlspatterns = [
    path('todos/', TodoListAPIView.as_view(), name='todos_list'),
]