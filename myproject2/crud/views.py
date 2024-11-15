from django.shortcuts import render
#HelloWorld を表示するために追加, ListViewはproduct_listのために追加、DetailViewは商品詳細追加のために追加
from django.views.generic import TemplateView, ListView, DetailView
# 新規作成フォーム追加、編集フォーム、削除フォーム追加時ににインポート
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# 商品一覧追加のためにインポート
from .models import Product
# 削除フォーム追加時にインポート
from django.urls import reverse_lazy
# ログインフォーム追加用に3行インポート
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

#top.htmlは相対パス
class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "list.html"
    paginate_by = 3

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    #デフォルトのTemplateファイル名が新規作成フォームと同じ「product_form.html」になるため、template_name_suffixで編集用のTemplateファイル名を指定するこの場合、Templateファイル名は「product_update_form.html」となる
    template_name_suffix = '_update_form'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('list')

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'
