from django.urls import reverse
from multiprocessing import context
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

#from hello.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'hello/index.html',context)

#def detail(request, question_id):
    #return HttpResponse(' Essa e a pergunta de numero {}'.format(question_id))

def results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'hello/results.html',{'question':question})
    #return HttpResponse(' Essa sao os resultado da pergunta de numero {}'.format(question_id))

def vote(request, question_id):
    #return HttpResponse(' Voce esta votando na questao de numero {}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'hello/vote.html', {
            'question': question,
            'error_message': "Voce nao selecionou",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('hello:results', args=(question.id,)))