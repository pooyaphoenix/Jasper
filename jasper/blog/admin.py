from django.contrib import admin

from .models import User , profile , Book , Field , Universty

@admin.register(User)
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
            'fields': ('name', 'description', 'master', 'status')
        }),
        ('second', {
             'fields': ('price', 'user', 'field', 'university')

        })
    )
    list_display = ('name', 'price', 'master', 'field', 'user','status','university')
    search_fields = ('name', 'master', 'field')

admin.site.register(Universty)

admin.site.register(profile)