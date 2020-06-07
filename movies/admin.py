from django.contrib import admin
from movies.models import AllMovies, Dipen, Ankur, Shantnu, Ashesh, Jayant, UpcomingReviews


class DisplayAdmin(admin.ModelAdmin): 
    list_display = ('post', 'reviewTitle', 'verdict', 'reviewDate')

admin.site.register(AllMovies)
admin.site.register(Dipen, DisplayAdmin)
admin.site.register(Ankur, DisplayAdmin)
admin.site.register(Shantnu, DisplayAdmin)
admin.site.register(Ashesh, DisplayAdmin)
admin.site.register(Jayant, DisplayAdmin)
admin.site.register(UpcomingReviews)


