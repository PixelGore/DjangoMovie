from django import forms
from django.contrib import admin
from django.utils.html import mark_safe
# Local imports
from .models import Category, Genre, Film, FilmStills, Actor, Rating, RatingStar, Reviews
#CKEditor
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Base
admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"


#CKEditor
class FilmAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Film
        fields = '__all__'


# Inlines
class RevewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class FilmStillsInLine(admin.TabularInline):
    model = FilmStills
    extra = 1
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"> ')

    get_image.short_description = "Image"


# Admin Classes
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    '''Film admin settings'''
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    list_editable = ("draft", )
    search_fields = ("title", "category__name")
    readonly_fields = ("get_poster", )
    actions = ["publish", "unpublish"]
    form = FilmAdminForm
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"), )
        }),
        (None, {
            "fields": ("description", ("poster", "get_poster"))
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"), )
        }),
        ("Actors", {
            "classes": ("collapse", ),
            "fields": (("actors", "directors", "genres", "category"), )
        }),
        (None, {
            "fields": (("budget", "box_office", "box_office_US"), )
        }),
        ("Options", {
            "fields": (("url", "draft"), )
        }),
    )
    inlines = [FilmStillsInLine, RevewInLine]
    save_on_top = True
    save_as = True

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="120" height="120"> ')

    get_poster.short_description = "Poster"

    def publish(self, request, querryset):
        '''Add a publication'''
        row_update = querryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 publication was updated"
        else:
            message_bit = f"{row_update} publications were updated"
        self.message_user(request, f"{message_bit}")
    publish.allowed_permissions = {'change', }

    def unpublish(self, request, querryset):
        '''Remove publication'''
        row_update = querryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 publication was updated"
        else:
            message_bit = f"{row_update} publications were updated"
        self.message_user(request, f"{message_bit}")
    unpublish.allowed_permissions = {'change', }


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    '''Actors or film director admin settings'''
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"> ')

    get_image.short_description = "Actor Image"


@admin.register(FilmStills)
class StillsAdmin(admin.ModelAdmin):
    '''Film Stills admin settings'''
    list_display = ("title", "film", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50">')

    get_image.short_description = "Stills of the film"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Category admin settings'''
    list_display = ("id", "name", "url")
    list_display_links = ("name", )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''Genres admin settings'''
    list_display = ("name", "url")


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    '''Reviews admin settings'''
    list_display = ("name", "email", "parent", "film", "id")
    readonly_fields = ("name", "email")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    '''Rating admin settings'''
    list_display = ("film", "ip", "star")


admin.site.register(RatingStar)
