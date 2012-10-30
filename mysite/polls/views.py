# Create your views here.
from django.template import RequestContext, loader, Context
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list':latest_poll_list,
    })
    return HttpResponse(t.render(c))
#    output = ', '.join([p.question for p in latest_poll_list])
#    return HttpResponse(output)
#    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
#    try:
    p = get_object_or_404(Poll, pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
    return render_to_response('polls/detail.html',{'poll': p}, context_instance = RequestContext(request))
#    return render_to_response('polls/detail.html',{'poll': p})
#    return HttpResponse("You're looking at poll %s." % poll_id)
 

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/detail.html',{
            'poll':p,
            'error_message':"You have not choiced yet.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

def results(request, poll_id):
    p=get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html',{'poll':p},context_instance = RequestContext(request))
