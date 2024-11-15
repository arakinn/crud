"""
URL configuration for myproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# HelloWorldを表示するために追加
from crud import views
# 画像表示のために2行追加
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # top はHelloworld、path(URL, クラス.as_view(), name=URLの名前)
    path('', views.TopView.as_view(), name="top"),
    # list は product_listのために追加
    path('crud/', views.ProductListView.as_view(), name="list"),
    # new は新規作成用フォームのために追加
    path('crud/new', views.ProductCreateView.as_view(), name="new"),
    # edit は編集フォームのために追加
    path('crud/edit/<int:pk>',views.ProductUpdateView.as_view(), name="edit"),
    # delete は削除フォームのために追加
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
    # 商品詳細ページのために追加
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),
    # ログインログアウト画面実装のために追加
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]

#「if settings.DEBUG:」と記述することで、開発モードの場合のみ静的ファイルを直接表示できるようにし、本番環境では不要な設定を回避できます。
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
