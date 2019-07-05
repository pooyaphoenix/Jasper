from django.contrib import admin
from django.contrib.auth.models import User
from .models import User2 , profile , Book , Field , Universty

@admin.register(User2)
class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','city','phone_number','description')

    fields = [
        'first_name'
        ,'last_name'
        , 'phone_number'
        , 'city'
    ]





@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name','status')





@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('status','field')
    fieldsets = (
        (None,{
            'fields': ('name', 'description', 'master', 'status','date_posted')
        }),
        ('second', {
             'fields': ('price', 'author', 'field', 'university')

        })
    )
    list_display = ('name', 'price', 'master', 'field', 'author','status','university')
    search_fields = ('name', 'master', 'field')

admin.site.register(Universty)

admin.site.register(profile)