from django.urls import path
from sistema_bancario_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:conta_id>/', views.index, name='index_id'),
    path('fazer_transacao/', views.fazer_transacao, name='fazer_transacao'),
    path('criar_conta/', views.criar_conta, name='criar_conta')
]