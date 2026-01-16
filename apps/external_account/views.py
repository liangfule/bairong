import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from apps.external_account.models import WecomInfo

#插件
def plugin_call(request):
    print(1)
    print(2)
    print(3)

# 查询渠道账号是否绑定
@require_GET
def query_wecom_account(request):
    company_name = request.GET.get('company_name')
    username = request.GET.get('username')

    if not company_name or not username:
        return JsonResponse({
            "code": 400,
            "msg": "company_name and username are required",
            "data": None
        })

    linked_account = (
        WecomInfo.objects
        .filter(
            company_name=request.GET.get('company_name'),
            username=request.GET.get('username'),
            is_delete=0
        ).annotate(
            robot_name=F('robot__robot_name'),
            robot_creator=F('robot__creator__username')
        )
        .values(
            'company_name',
            'username',
            'robot_id',
            'robot_name',
            'robot_creator'
        )
    )

    query_result = {
        "code": 0,
        "msg": "success",
        "data": list(linked_account)
    }

    return JsonResponse(query_result)


# 解除绑定关系
@require_POST
@csrf_exempt
def del_wecom_account(request):
    try:
        robot_id = json.loads(request.body.decode('utf-8'))['robot_id']
    except json.decoder.JSONDecodeError:
        return JsonResponse({
            "code": 400,
            "msg": "参数异常！",
            "data": None
        })

    if not robot_id:
        return JsonResponse({
            "code": 400,
            "msg": "robot_id are required",
            "data": None
        })

    is_exist = WecomInfo.objects.filter(robot_id=robot_id, is_delete=0).exists()

    if not is_exist:
        return JsonResponse({
            "code": 0,
            "msg": "当前企业微信账号不存在绑定agent！",
            "data": None
        })
    else:

        WecomInfo.objects.filter(robot_id=robot_id).update(is_delete=1)

        return JsonResponse({
            "code": 0,
            "msg": "解绑成功！",
            "data": None
        })
