from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
import json
from .models import Category
from .forms import CategoryForm

# TODO: ホーム画面にカテゴリー毎の累計活動時間の表示
    #* activity:HomeView内でimportする必要あり
    #* カテゴリーが削除済み(is_deleted = Ture)の場合は表示しない

# TODO: カテゴリー毎のhome画面
    #* カテゴリー毎の累計時間・累計日数の表示
    #* グラフの表示に必要なjson型データの送信

# TODO: カテゴリー作成機能
    #* activity:HomeViewでimportする必要あり
    #* home内でカテゴリー追加モーダルを表示(カテゴリー名・目標・色を選択)
# カテゴリー作成機能
class CategoryAddView(LoginRequiredMixin, generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('activity:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# 同じ名前のカテゴリーが存在するか確認
def check_duplicate(request):
    if request.method == "POST":
        data = json.loads(request.body)
        category_name = data.get("name")
        existing_category = Category.objects.filter(user=request.user, name=category_name)
        deleted_category = existing_category.filter(is_deleted=True).first()

        if deleted_category:
            return JsonResponse({"duplicate": True, "category_id": deleted_category.id})
        elif existing_category.exists():
            return JsonResponse({"duplicate": True, "category_id": None})
        else:
            return JsonResponse({"duplicate": False})
    else:
        return JsonResponse({"error": "Invalid request method"})

# カテゴリー復元
def category_restore(request, pk):
    category = Category.objects.get(pk=pk, user=request.user)
    category.is_deleted = False
    category.save()
    return HttpResponseRedirect(reverse_lazy('activity:home'))


# カテゴリー復元
def category_restore(request, pk):
    category = Category.objects.get(pk=pk, user=request.user)
    category.is_deleted = False
    category.save()
    return HttpResponseRedirect(reverse_lazy('activity:home'))

# TODO: カテゴリーの編集
    #* カテゴリー毎のhome画面でモーダルで表示(カテゴリー名・目標・選択)

# TODO: カテゴリーの削除機能
    #* カテゴリー毎のhome画面で削除モーダルを表示し削除
    #* カテゴリー削除はis_deletedをtureに変更
