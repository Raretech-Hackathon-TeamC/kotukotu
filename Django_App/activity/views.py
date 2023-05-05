from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ActivityRecord
from .forms import ActivityRecordForm
from . import models
from . import graph
import datetime
from collections import defaultdict

# ホーム画面(仮)
# Todo: 未完了
class HomeView(LoginRequiredMixin, generic.TemplateView):
    #テンプレートファイル連携
    template_name = 'home.html'
    
    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):
        # ページを表示している日付を取得
        today = datetime.date.today()
        # ページを表示している日付から7日分の日付を取得
        date_list = [today - datetime.timedelta(days=x) for x in range(6, -1, -1)]
        date_list.reverse()
        # グラフのデータを取得
        qs = models.ActivityRecord.objects.filter(date__in=date_list)  
        # 同じ日付のデータを合算するための辞書を用意
        duration_dict = defaultdict(int)
        for activity in qs:
            duration_dict[activity.date] += activity.duration
        # グラフに反映するためのデータを作成
        x = []      #X軸データ
        y = []      #Y軸データ
        for date in date_list:
            x.append(date)
            y.append(duration_dict.get(date, 0)) #データが存在しない場合は0を代入
        chart = graph.Plot_Graph(x,y) #グラフ作成
        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
        return context

    #get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

# 積み上げ追加画面
class ActivityAddView(LoginRequiredMixin, generic.CreateView):
    model = ActivityRecord
    form_class = ActivityRecordForm
    template_name = 'activity_add.html'
    success_url = reverse_lazy('activity:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
