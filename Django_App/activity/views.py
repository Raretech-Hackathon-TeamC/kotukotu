from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ActivityRecord
from .forms import ActivityRecordForm

# ホーム画面(仮)
# Todo: 未完了
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'

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
# Todo: 未完了
class ActivityEditView(LoginRequiredMixin, generic.UpdateView):
    model = ActivityRecord
    form_class = ActivityRecordForm
    template_name = 'activity_edit.html'
    success_url = reverse_lazy('activity_list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

# 積み上げ削除画面
# Todo: 未完了
class ActivityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ActivityRecord
    template_name = 'activity_delete.html'
    success_url = reverse_lazy('activity_list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
