from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Question, Choice

# Methods will be called when the url handler
# (urls.py) sends it.

# Proper way to render using templates (avoids unnecessary imports, too)
def index(request):
    q_list = Question.objects.order_by('-pub_date')[:5]
    # expose variables to the inline code
    context = {'latest_question_list': q_list}
    # params: request, template location, variable exposures
    return render(request, 'polls/index.html', context);
    
def details(request, question_id):
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    
    # OR
    
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': q})
    
# Build and render the page manually - not recommended
def results(request, question_id):
    q_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': q_list,
    })
    return HttpResponse(template.render(context))
    
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))