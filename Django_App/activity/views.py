from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ActivityRecord
from .forms import ActivityRecordForm

# ホーム画面(仮)
# Todo: 未完了
class HomeView(LoginRequiredMixin, generic.TemplateView):
    #テンプレートファイル連携
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = ActivityRecord.objects.all()
        date_list = [record.date.strftime('%-m/%-d') for record in records]
        duration_list = [record.duration for record in records]
        duration_list = [round(record.duration / 60, 2) for record in records] # 分単位から小数点第２位の時間に変換
        context['date_list'] = date_list
        context['duration_list'] = duration_list
        return context


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
