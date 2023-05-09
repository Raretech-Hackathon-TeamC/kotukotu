from django.db import models
from django.conf import settings

class ActivityRecord(models.Model):
    """
    ActivityRecord

    - id (PK): 主キー
    - user_id (FK - users): usersテーブルを参照（外部キー）
    - date: 記録された日付 (例: '2023-04-04')
    - duration: 活動時間（分） (例: 360)
    - memo: メモ (例: '今日は集中して勉強できた')
    - created_at: レコード作成日時 (例: '2023-04-04 10:30:00')
    - updated_at: レコード更新日時 (例: '2023-04-04 10:30:00')
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date = models.DateField()
    duration = models.PositiveIntegerField()
    memo = models.TextField(blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 日付を降順でソート
        ordering = ['-date']

    def __str__(self):
        return f"{self.user} - {self.duration}m on {self.date}"
