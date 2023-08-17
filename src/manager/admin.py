from django.contrib import admin

from manager.models import Book, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    prepopulated_fields = {"title": ("text",)}
    # list_display = ['title', 'date']
    search_fields = ['title']
    list_filter = ['date', 'authors']
    readonly_fields = ["count_likes", 'order_number']

    # filter_horizontal = ('likes',)
    # filter_vertical = ('likes',)
    # fieldsets = [
    #     (
    #         'heello',
    #         {
    #             "fields": ["text", "title", "authors"],
    #         },
    #     ),
    #     (
    #         "Advanced options",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ["count_likes"],
    #         },
    #     ),
    # ]

    def order_number(self, obj):
        return obj.id

    order_number.short_description = 'Номер заказа'



admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
