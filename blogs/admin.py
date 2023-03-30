from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Tags, Category


class ArticleAdmin(admin.ModelAdmin):

    # 定义一个方法
    def riqi(self):
        return self.created_time.strftime("%b %d %Y %H:%M:%S")
    # 设置方法字段在admin中显示的标题
    riqi.short_description = '发布日期'

    # 定义关联对象字段
    def category_en(self):
        return self.category.name_en

    category_en.short_description = '分类英文'

    list_display = ('id', 'title', 'intro', 'category', category_en, 'created_time', riqi)
    list_display_links = ('title',)
    # fk_fields 设置显示外键字段
    fk_fields = ['category']
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 3
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_time',)

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    # list_editable = ['title', 'user']

    # 列表顶部，设置为False不在顶部显示，默认为True。
    # actions_on_top = True

    # 列表底部，设置为False不在底部显示，默认为False。
    # actions_on_bottom = False

    # 定制Action行为具体方法
    def updateCreateTime(self, request, queryset):
        queryset.update(created_time='2018-09-28')
        # 批量更新我们的created_time字段的值为2018-09-28

    def updateCategory(self, request, queryset):
        queryset.update(category='3')

    updateCreateTime.short_description = "更新创建时间"
    updateCategory.short_description = "更新分类"
    actions = [updateCreateTime, updateCategory]

    search_fields = ['title', 'intro']  # 搜索框
    list_filter = ['user']  # 右侧栏过滤器，按作者进行筛选


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
