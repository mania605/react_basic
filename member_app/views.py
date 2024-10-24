from django.http import HttpResponse
from django.template import loader
from .models import Member

# 메인 화면 출력 응답 함수
def home(request):
  return HttpResponse(loader.get_template('home.html').render())

# member 화면 출력 응답 함수
def members(request):
  members = Member.objects.all().values()
  context = {'members':members}
  return HttpResponse(loader.get_template('members.html').render(context, request))

# 멤버 상세정보 템플릿 출력 응답 함수
def details(request, id):
  member = Member.objects.get(id=id)
  context = {'member':member}
  return HttpResponse(loader.get_template('details.html').render(context, request))



