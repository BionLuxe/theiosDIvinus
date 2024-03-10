from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    banner = Banners.objects.all()
    sermonss = VideoSermons.objects.all()
    events = Events.objects.all()
    new = News.objects.all()
    ministry = Ministries.objects.all()
    quote = Quotes.objects.all()
    videoBanner = VideoBanners.objects.all()
    context = {
        "banner": banner,
        "sermonss": sermonss,
        "events": events,
        "new": new,
        "ministry": ministry,
        "quote": quote,
        "videoBanner": videoBanner,
    }
    return render(request, 'index.html',context)


def contact(request):
    return render(request, 'contact.html')

def event(request):
    events = Events.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'events.html', context)

def gGallery(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery": gallery,
    }
    return render(request, 'gallery.html', context)

def news(request):
    new = News.objects.all()
    context = {
        "new":new
    }
    return render(request, 'news.html',context)
    
def newdetails(request,news_id):
    details = get_object_or_404(News, pk=news_id)
    context = {
        "details":details
    }   
    return render(request, 'newsdetails.html', context)
def eventdetails(request,id):
    eventdetails = get_object_or_404(Events, id=id)
    context = {
        "eventdetails":eventdetails
    }   
    return render(request, 'eventdetails.html', context)

def memberdetails(request,memberdetails_id):
    memberdetails = get_object_or_404(OurStaff, id=memberdetails_id)

    context = {
        "memberdetails": memberdetails,
    }   
    return render(request, 'memberdetails.html', context)

def ministrydetails(request,ministrydetails_id):
    ministrydetails = get_object_or_404(Ministries, pk=ministrydetails_id)
    context = {
        "ministrydetails": ministrydetails
    }   
    return render(request, 'ministrydetails.html', context)

def projects(request):
    project = OngoingProjects.objects.all()
    context = {
        "project":project,
    }
    return render(request, 'projects.html', context)

def detail_view(request, id=None):
    post = get_object_or_404(OngoingProjects, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post':post,
        'photos':photos
    })


def futureprojects(request):
    return render(request, 'futureprojects.html')

def sermons(request):
    sermon = VideoSermons.objects.all()
    audio = EnglishAudioSermons.objects.all()
    lugandaaudio =  LugandaAudioSermons.objects.all()
    context = {
        'sermon':sermon,
        'audio':audio,
        'lugandaaudio':lugandaaudio
    }
    return render(request, 'sermons.html',context)

def donate(request):
    return render(request, 'donate.html')




def history(request):
    ourhistory = OurHistory.objects.all()
    context = {
        "ourhistory": ourhistory
    }   
    return render(request, 'history.html', context)

def vision(request):
    ourvision = Vision.objects.all()
    context = {
        "ourvision": ourvision
    }   
    return render(request, 'vision.html', context)

def whatwebelieve(request):
    ourwhatwebelieve = Whatwebelieve.objects.all()
    context = {
        "ourwhatwebelieve": ourwhatwebelieve
    }   
    return render(request, 'whatwebelieve.html', context)

def ministryname(request):
    ourministryname = MinistryName.objects.all()
    context = {
        "ourministryname": ourministryname
    }   
    return render(request, 'ourministryname.html', context)

def servicetimes(request):
    service = Servicetimes.objects.all()
    context = {
        "service": service
    }   
    return render(request, 'whatwebelieve.html', context)

def tdaccf(request):
    tdac = Tdaccf.objects.all()
    context = {
        "tdac": tdac
    }   
    return render(request, 'tdac.html', context)
def staff(request):
    member = OurStaff.objects.all()
    context = {
        "member": member
    }   
    return render(request, 'staff.html', context)

def testimonials(request):
    testify = Testimonials.objects.all()
    context = {
        "testify": testify,
    }
    return render(request, 'testify.html', context)

def testimonydetails(request,testimonydetails_id):
    testimonydetails = get_object_or_404(Testimonials, id=testimonydetails_id)
    testimonyphotos = TestimonyImages.objects.filter(post=testimonydetails)
    context = {
        "testimonydetails": testimonydetails,
        "testimonyphotos":  testimonyphotos ,
    }   
    return render(request, 'testimonydetails.html', context)

def questions(request):
    context = {
    }
    return render(request, 'questions.html',context)

def top20(request):
    top20Questions = Question.objects.order_by('-date')[:20]
    newquestions = top20Questions = Question.objects.order_by('-date')
    context = {
        'top20Questions': top20Questions,
    }
    return render(request, 'top20.html',context)

def article(request):
    aericle = Articles.objects.all
    context = {
        'aericle': aericle,
    }
    return render(request, 'articles.html',context)

def whatsnew(request):
    newquestions  = Question.objects.order_by('-date')
    context = {
        'newquestions': newquestions,
    }
    return render(request, 'whatsnew.html',context)
def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'answer.html', context)


def search(request):
    query = request.GET.get('q', '')  # Retrieve the search query from the request

    # Perform a case-insensitive search on the question field
    search_results = Question.objects.filter(question__icontains=query)

    context = {
        'query': query,
        'search_results': search_results,
    }

    return render(request, 'search_results.html', context)