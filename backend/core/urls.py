from django.urls import path
from .views import *

urlpatterns = [
    path('faturamento/previa', FaturamentoView.as_view(), name='previa'),
    path('faturamento/previa/<int:pk>/', FaturamentoItemView.as_view(), name='previaItem'),
    
    path('faturamento/item/<int:pk>/', FaturamentoIdView.as_view(), name='previaID'),
    path('faturamento/itemconfig/<int:pk>/', ItemConfigIdView.as_view(), name='ItemConfigID'),
        
    path('faturamento/previa/conteudo/<int:id>',
         ItemConteudoView.as_view(), name='conteudoItem'),  
]