from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic.base import RedirectView
sitemaps = {
    'index': StaticViewSitemap,
    'ministries': MinistriesSitemap,
    'banners': BannersSitemap,
    'video_sermons': VideoSermonsSitemap,
    'english_audio_sermons': EnglishAudioSermonsSitemap,
    'luganda_audio_sermons': LugandaAudioSermonsSitemap,
    'events': EventsSitemap,
    'news': NewsSitemap,
    'members': MembersSitemap,
    'ongoing_projects': OngoingProjectsSitemap,
    'quotes': QuotesSitemap,
}

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), 
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gGallery, name='gallery'),
    path('testify', views.testimonials, name='testify'),
    path('tdaccf', views.tdaccf, name='tdaccf'),
    path('staff', views.staff, name='staff'),
    path('event', views.event, name='event'),
    path('news', views.news, name='news'),
    path('sermons', views.sermons, name='sermons'),
    path('history', views.history, name='history'),
    path('vision', views.vision, name='vision'),
    path('top20', views.top20, name='top20'),
    path('whatsnew', views.whatsnew, name='whatsnew'),
    path('article', views.article, name='article'),
    path('whatwebelieve', views.whatwebelieve, name='whatwebelieve'),
    path('ministryname', views.ministryname, name='ministryname'),
    path('projects', views.projects, name='projects'),
    path('futureprojects', views.futureprojects, name='futureprojects'),
    path('donate', views.donate, name='donate'),
    path('questions', views.questions, name='questions'),
    path('<int:id>/', views.detail_view, name='detail'),
    path('staff/<int:memberdetails_id>/', views.memberdetails, name='memberdetails'),
    path('ministries/<int:ministrydetails_id>/', views.ministrydetails, name='ministrydetails'),
    path('news/<int:news_id>/', views.newdetails, name='newdetails'),
    path('testimonydetail/<int:testimonydetails_id>/', views.testimonydetails, name='testimonydetail'),
    path('answer/<int:question_id>/', views.answer, name='answer'),
    path('search/', views.search, name='search'),
    ]