from django.urls import path
from .views import TaskListView, MyLoginView, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, MyRegisterPage
from django.contrib.auth.views import LogoutView
from .forms import CustomLoginForm


urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('login/', MyLoginView.as_view(authentication_form=CustomLoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', MyRegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')
    # path('register/',)


]