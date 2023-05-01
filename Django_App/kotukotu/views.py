from django.shortcuts import render

# Create your views here.
# ほそまつが確認用にいれました。
def test_tailwind(request):
    return render(request, 'kotukotu/test_tailwind.html')