from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.template import loader
from django.views import generic
from polls.models import Question
import json

def index(request):
    latest_question_list = list(Question.objects.order_by('-pub_date').values())
    template = loader.get_template('polls/index.html')
    context = {'latestQuestionList': json.dumps(latest_question_list, cls=DjangoJSONEncoder)}
    
    return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.all
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)