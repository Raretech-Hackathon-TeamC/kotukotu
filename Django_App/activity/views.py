from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import JsonResponse
from .models import ActivityRecord
from .forms import ActivityRecordForm

# ホーム画面
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'   #テンプレートファイル連携

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.user_name   # Usersからユーザー名前を取得
        records = ActivityRecord.objects.all()   # ActivityRecordの全てのデータを取得する
        date_list = [record.date.strftime('%-m/%-d') for record in records]  # 日付のリストを作成し、'%-m/%-d'のフォーマットに変換する
        duration_list = [record.duration for record in records]   # 各レコードのdurationをduration_listに格納する
        total_duration = sum(duration_list) // 60, sum(duration_list) % 60  # duration_listから総時間を計算する
        total_duration_str = f"{total_duration[0]}時間{total_duration[1]}分" # 計算結果を'時間:分'の形式に変換してtotal_duration_strに格納する
        total_days = len(set(date_list))   # date_listから総日数を計算する
        duration_list = [round(record.duration / 60, 2) for record in records] # duration_listから各durationを'時間.分'の形式に変換してduration_listに格納する

        # コンテキストに必要な変数を格納し、returnする
        context['date_list'] = date_list
        context['duration_list'] = duration_list
        context['total_duration'] = total_duration_str
        context['total_days'] = total_days
        return context


# 積み上げ追加画面
class ActivityAddView(LoginRequiredMixin, generic.CreateView):
    # モデル・フォーム・テンプレート・リダイレクト先の設定
    model = ActivityRecord
    form_class = ActivityRecordForm
    template_name = 'activity_add.html'
    success_url = reverse_lazy('activity:home')

    # フォームが有効な場合、リクエストユーザーを設定
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # POSTリクエストの場合、ajax_submitメソッドを呼び出す
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.ajax_submit(request)
        # それ以外の場合、親クラスのdispatchメソッドを呼び出す
        return super(ActivityAddView, self).dispatch(request, *args, **kwargs)

    # ajax_submitメソッド(非同期通信で、)
    def ajax_submit(self, request):
        # リクエストからフォームを作成
        form = self.form_class(request.POST, instance=ActivityRecord(user=request.user))

        # フォームが有効な場合、保存し成功メッセージを返す
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        # フォームが無効な場合、エラーメッセージを返す
        else:
            return JsonResponse({"success": False, "errors": form.errors})

# 累計日数の取得
def get_total_days(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    # 日付を一意にしたデータセットを取得
    unique_dates = ActivityRecord.objects.filter(user=user).values('date').annotate(count=Count('date'))

    # 一意な日付の数をカウント
    total_days = len(unique_dates)

    return JsonResponse({"total_days": total_days})

# レコード画面(積み上げ一覧)
class ActivityListView(LoginRequiredMixin, generic.ListView):
    model = ActivityRecord
    template_name = 'activity_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# 積み上げ編集画面
class ActivityEditView(LoginRequiredMixin, generic.UpdateView):
    model = ActivityRecord
    form_class = ActivityRecordForm
    template_name = 'activity_edit.html'
    success_url = reverse_lazy('activity:activity_list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

# 積み上げ削除画面
class ActivityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ActivityRecord
    success_url = reverse_lazy('activity:activity_list')

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
