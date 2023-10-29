from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    
    return render(request, 'core/index.html')

# @login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'core/topics.html', context)

# @login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'core/topic.html', context)

# @login_required
def newtopic(request):
    if request.method != 'POST':
        form = TopicForm()
        
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            newtopic = form.save(commit=False)
            newtopic.owner= request.user
            newtopic.save()
            return redirect('core:topics')
        
    context = {'form': form}
    return render(request, 'core/newtopic.html', context)

# @login_required
def newentry(request, topic_id):
    topic =Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
       form = EntryForm()
       
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            newentry= form.save(commit=False)
            newentry.topic = topic
            newentry.save()
            return redirect('core:topic', topic_id=topic_id)
        
    context = {'topic':topic, 'form':form}
    return render(request, 'core/newentry.html', context)
# @login_required
def editentry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
        
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:topic', topic_id=topic.id)
        
    context = {'entry':entry, 'topic': topic, 'form':form}
    return render(request, 'core/editentry.html', context)
        