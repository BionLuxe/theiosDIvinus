from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Aboutus, Banners, VideoSermons, EnglishAudioSermons, LugandaAudioSermons, Events, News, OurStaff, OngoingProjects, Ministries, Quotes

class StaticViewSitemap(Sitemap):
    """
    Adds static views to sitemap
    """
    def items(self):
        return ['index']

    def location(self, item):
        return reverse('index')
class MinistriesSitemap(Sitemap):
    """
    Adds Ministries page to sitemap
    """
    def items(self):
        return Ministries.objects.all()

    def location(self, item):
        return reverse('ministrydetails')


class BannersSitemap(Sitemap):
    """
    Adds Banners page to sitemap
    """
    def items(self):
        return Banners.objects.all()

    def location(self, item):
        return reverse('index')


class VideoSermonsSitemap(Sitemap):
    """
    Adds VideoSermons page to sitemap
    """
    def items(self):
        return VideoSermons.objects.all()

    def location(self, item):
        return reverse('sermons')


class EnglishAudioSermonsSitemap(Sitemap):
    """
    Adds EnglishAudioSermons page to sitemap
    """
    def items(self):
        return EnglishAudioSermons.objects.all()

    def location(self, item):
        return reverse('sermons')


class LugandaAudioSermonsSitemap(Sitemap):
    """
    Adds LugandaAudioSermons page to sitemap
    """
    def items(self):
        return LugandaAudioSermons.objects.all()

    def location(self, item):
        return reverse('sermons')


class EventsSitemap(Sitemap):
    """
    Adds Events page to sitemap
    """
    def items(self):
        return Events.objects.all()

    def location(self, item):
        return reverse('eventdetails')


class NewsSitemap(Sitemap):
    """
    Adds News page to sitemap
    """
    def items(self):
        return News.objects.all()

    def location(self, item):
        return reverse('news')


class MembersSitemap(Sitemap):
    """
    Adds Members page to sitemap
    """
    def items(self):
        return OurStaff.objects.all()

    def location(self, item):
        return reverse('memberdetails')


class OngoingProjectsSitemap(Sitemap):
    """
    Adds OngoingProjects page to sitemap
    """
    def items(self):
        return OngoingProjects.objects.all()

    def location(self, item):
        return reverse('projects')




class QuotesSitemap(Sitemap):
    """
    Adds Quotes page to sitemap
    """
    def items(self):
        return Quotes.objects.all()

    def location(self, item):
        return reverse('index')
