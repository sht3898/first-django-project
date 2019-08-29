from django.shortcuts import render

# Create your views here.
def push(request):
    # 사용자에게 form을 전송한다.
    return render(request, 'num/push.html')


def pull(request):
    # 사용자가 입력한 값을 받는다.
    num = request.GET.get('num')
    context = {
        'num' : num
    }
    return render(request, 'num/pull.html', context)