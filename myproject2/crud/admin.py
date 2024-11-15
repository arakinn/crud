from django.contrib import admin
#admin 画面に商品を表示するために追加、カテゴリ追加時に Category を追加
from .models import Product, Category
#HTMLで画像を表示するにはimgタグを使用します。管理画面にimgタグを出力するためにmark_safe関数を使用します。このmark_safe関数は指定した文字列が安全であるという印をつけて、HTMLを出力します。
from django.utils.safestring import mark_safe

# Register your models here.


# admin 画面にID、名前、価格を表示して検索欄を追加
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image', 'detail')
    search_fields = ('name',)
    list_filter = ('category',)

    # 画像用に追加
    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

#admin 画面に商品を表示するために追加, ID名前等を追加した際にProductAdminを追加
admin.site.register(Product, ProductAdmin)
# admin 画面にカテゴリを表示するために追加
admin.site.register(Category, CategoryAdmin)

