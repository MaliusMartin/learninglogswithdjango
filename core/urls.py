
from django.urls import path

from core.views import index, topics, topic,newtopic, newentry, editentry

app_name = 'core'

urlpatterns = [
    
    path('', index, name='index'),
    path('topics/', topics, name='topics'),
    path('newtopic/', newtopic, name='newtopic'),
    path('topics/<int:topic_id>/', topic, name='topic'),
    path('newentry/<int:topic_id>/',newentry, name='newentry'),
    path('editentry/<int:entry_id>', editentry, name='editentry')
    
]
