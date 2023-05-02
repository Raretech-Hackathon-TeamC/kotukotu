from django.core.exceptions import ValidationError
import re

# 自作バリデーション
class CustomPasswordValidator():
  # バリデーションメッセージ
  msg = 'パスワードには、0-9, a-z, 記号(#$%&)を含めてください'

  def __init__(self):
    pass

  # passwordに対してのキーワード検索
  def validate(self,password,user=None):
    if all(
      (re.search('[0-9]', password), 
      re.search('[a-z]', password), 
      re.search('[#$%&]', password))):
      return
    raise ValidationError(self.msg)

  def get_help_text(self):
    return self.msg