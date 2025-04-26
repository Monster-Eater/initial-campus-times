from django.contrib import admin
from .models import Event
from .models import Venue
from .models import MyClubUser, Donate, Category, Comment
from .models import Profile, Meep, Complaint, Video
from django.contrib.auth.models import User, Group

admin.site.unregister (Group)
admin.site.register(Profile)
admin.site.register(MyClubUser)
admin.site.register(Complaint)
admin.site.register(Donate)
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Comment)

class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User    
    fields = ['username']
    inlines = [ProfileInline]

admin.site.unregister (User)   
admin.site.register(User, UserAdmin)
admin.site.register(Meep)
   


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone")
    ordering = ("name",)
    search_fields = ("name", "address")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (("name", "venue"), 'event_date', 'description', 'manager' )
    list_display = ('name', "event_date", "venue") 
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)

