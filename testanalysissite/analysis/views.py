# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.core.files.storage import default_strage
from analysis.models import Subject, Experiment
from numpy import *
from matplotlib import pylab
from pylab import *
from scipy.io import loadmat
#import PIL, PIL.Image, StringIO

def index(request):
	number_subject = Subject.objects.all()
#	t = loader.get_template('analysis/index.html')
	return render_to_response('analysis/index.html', {
		'numsub': number_subject,
	}, context_instance=RequestContext(request))
#	return HttpResponse(reverse('analysis.views.detail',args=(number_subject.id,)))

def selectsub(request):
	s = get_object_or_404(Subject,pk=request.POST['subject'])
	return HttpResponseRedirect(reverse('analysis.views.detail',args=(s.id,)))

def detail(request,sub_id):
#	number_exp = get_object_or_404(Experiment, subject=sub_id)
	number_exp = Experiment.objects.filter(subject=sub_id)
#	t = loader.get_template('analysis/detail.html')
	return render_to_response('analysis/detail.html', {
		'numexp': number_exp,
		'subid': sub_id,
	}, context_instance=RequestContext(request))
#	return HttpResponse(reverse('analysis.views.detail',args=(number_subject.id,)))

def selectexp(request,sub_id):
	e = Experiment.objects.get(subject=sub_id,pk=request.POST['experiment'])
#	return HttpResponseRedirect(reverse('analysis.views.dataview',args=(sub_id,e.exp_date.strftime('%Y%m%d'),)))
	return HttpResponseRedirect(reverse('analysis.views.dataview',args=(sub_id,e.id,)))

def dataview(request,sub_id,exp_id):
	t = loader.get_template('analysis/dataview.html')
	c = Context({
		'plotfigure': "Yes",
	})
	return HttpResponse(t.render(c))
	
def plotrawsignal(request,sub_id,exp_id):
	e 			= Experiment.objects.get(pk=exp_id, subject=sub_id)
	dataPath 	= e.exp_datapath
	dataset 	= loadmat(dataPath) 
	sourcedata 	= dataset['y']
	response 	= HttpResponse(content_type="image/png")
	figure(figsize=(8,3))
	
	subplot(211)
	plot(sourcedata[0],sourcedata[1])
	title(dataPath)
	ylim(-50, 50)

	subplot(212)
	plot(sourcedata[0],sourcedata[14])

	savefig(response,format="png");
	
#	response=HttpResponse("Hello")
	return response

def tfmap(request,sub_id,exp_id):
	e 			= Experiment.objects.get(pk=exp_id, subject=sub_id)
	dataPath 	= e.exp_datapath
	dataset 	= loadmat(dataPath) 
	sourcedata 	= dataset['y']
	
	fftsignal 	= abs(fft(sourcedata[1]))
	fs 			= 256
	data1 		= sourcedata[1]
	trig 		= sourcedata[14]

	trigpos 	= find(trig[1:len(trig)]-trig[0:len(trig)-1]==0.5)

	data4fft	= data1[trigpos[0]-fs:trigpos[1]+fs]

	framesz 	= 1.0
	hop  	  	= 0.1
	framesamp 	= int(framesz*fs)
	hopsamp   	= int(hop*fs)
	w  		  	= hamming(framesamp)
	fftdata   	= zeros((len(range(0, len(data4fft)-framesamp, hopsamp)),fs))
	counter   	= 0
	for i in range(0, len(data4fft)-framesamp, hopsamp):
		fftdata[[counter]] = array([abs(fft(w*data4fft[i:i+framesamp]))])
		counter +=1

	figure(figsize=(8,3))
	imshow(transpose(fftdata[:,1:40]))

	axis('tight')
	response = HttpResponse(content_type="image/png")
	savefig(response, format="png");

	return response
	
def tpplot(request,sub_id,exp_id):
	e 			= Experiment.objects.get(pk=exp_id, subject=sub_id)
	dataPath 	= e.exp_datapath
	dataset 	= loadmat(dataPath) 
	sourcedata 	= dataset['y']
	
	fftsignal 	= abs(fft(sourcedata[1]))
	fs 			= 256
	data1 		= sourcedata[1]
	trig 		= sourcedata[14]

	trigpos 	= find(trig[1:len(trig)]-trig[0:len(trig)-1]==0.5)

	data4fft	= data1[trigpos[0]-fs:trigpos[1]+fs]

	framesz 	= 1.0
	hop  	  	= 0.1
	framesamp 	= int(framesz*fs)
	hopsamp   	= int(hop*fs)
	w  		  	= hamming(framesamp)
	fftdata   	= zeros((len(range(0, len(data4fft)-framesamp, hopsamp)),fs))
	counter   	= 0
	for i in range(0, len(data4fft)-framesamp, hopsamp):
		fftdata[[counter]] = array([abs(fft(w*data4fft[i:i+framesamp]))])
		counter +=1

	figure(figsize=(8,3))
	plot(mean(fftdata[:,8:12],1))

	axis('tight')
	response = HttpResponse(content_type="image/png")
	savefig(response, format="png");
	
	return response