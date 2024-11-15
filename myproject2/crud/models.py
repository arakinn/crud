from django.db import models
# reverse を新規作成フォームで使うためにインポート
from django.urls import reverse

# Create your models here.
# カテゴリを追加
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    # 商品名を文字列型で定義する最大文字列長は200
    name = models.CharField(max_length=200)
    # 金額を正の整数型で定義する  
    price = models.PositiveIntegerField()
    # カテゴリを追加
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 画像を追加
    img = models.ImageField(blank=True, default='noImage.png')
    # 商品説明を追加
    detail = models.TextField(blank=True, null=True)

    # adminの一覧画面でProductの名前が表示されるようにする
    def __str__(self):
        return self.name
    
        # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')