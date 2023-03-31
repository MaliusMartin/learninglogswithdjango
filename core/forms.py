from django import forms 

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic 
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['headline','text' ]
        labels = {'text': 'Entry:', 'headline': 'heading'}
        widgets = {'headline': forms.CharField(max_length=150, required=True)}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
       
