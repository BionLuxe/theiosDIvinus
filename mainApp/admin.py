from django.contrib import admin
from .models import Articles,Question,Testimonials,TestimonyImages,Gallery,OurStaff,Tdaccf,Ministries,MinistryName,Servicetimes,Vision, Whatwebelieve,OurHistory,VideoBanners,Quotes,PostImage,OngoingProjects,Aboutus,Banners,VideoSermons,News,Events,EnglishAudioSermons,LugandaAudioSermons
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Banners)
admin.site.register(VideoSermons)
admin.site.register(Events)
admin.site.register(EnglishAudioSermons)
admin.site.register(LugandaAudioSermons)
admin.site.register(Quotes)
# admin.site.register(VideoBanners)
admin.site.register(Gallery)

class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(OngoingProjects)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = OngoingProjects
 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass



# class SomeModelAdmin(SummernoteModelAdmin):  
#     summernote_fields = '__all__'

# admin.site.register(Aboutus, SomeModelAdmin)

class PostMinistry(SummernoteModelAdmin):
    summernote_fields = ('details',)

admin.site.register(Ministries, PostMinistry)

class Background(SummernoteModelAdmin):
    summernote_fields = ('background',)

admin.site.register(OurHistory, Background)

class WhatWeBelieve(SummernoteModelAdmin):
    summernote_fields = ('what_we_believe',)

admin.site.register(Whatwebelieve, WhatWeBelieve)

class Vision1(SummernoteModelAdmin):
    summernote_fields = ('vision',)

admin.site.register(Vision, Vision1)

class Servicetime(SummernoteModelAdmin):
    summernote_fields = ('servicetimes',)

admin.site.register(Servicetimes, Servicetime)

class MinistryName1(SummernoteModelAdmin):
    summernote_fields = ('ministryName',)

admin.site.register(MinistryName, MinistryName1)

class TDACCF1(SummernoteModelAdmin):
    summernote_fields = ('TDACCF',)

admin.site.register(Tdaccf, TDACCF1)

class staff(SummernoteModelAdmin):
    summernote_fields = ('member_biography',)

admin.site.register(OurStaff, staff)

class new(SummernoteModelAdmin):
    pass

admin.site.register(News, new)

class question(SummernoteModelAdmin):
    summernote_fields = ('answer',)

admin.site.register(Question, question)

admin.site.register(Articles, question)


class PostTestimonyImageAdmin(admin.StackedInline):
    model = TestimonyImages
 
@admin.register(Testimonials)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostTestimonyImageAdmin]
 
    class Meta:
       model = Testimonials
 
@admin.register(TestimonyImages)
class PostTestimonyImageAdmin(admin.ModelAdmin):
    pass
