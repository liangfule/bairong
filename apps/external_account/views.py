import json

from django.db.models import F
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from apps.external_account.models import WecomInfo, RobotIdMap


# 测试查询
def test_function(request):
    print('请求成功！')
    return JsonResponse({
        "code": 0,
        "msg": "~~okk~~",
        "data": None
    })


# 查询企微账号是否绑定
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
            company_name=company_name,
            username=username,
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


# 解除企微账号绑定关系
@require_POST
@csrf_exempt
def del_wecom_account(request):
    try:
        body = json.loads(request.body or "{}")
        robot_id = body.get("robot_id")
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
            "msg": "当前企业微信账号不存在绑定的agent！",
            "data": None
        })
    else:

        WecomInfo.objects.filter(robot_id=robot_id).update(is_delete=1)

        return JsonResponse({
            "code": 0,
            "msg": "解绑成功！",
            "data": None
        })


# 查询钉钉账号是否绑定
@require_GET
def query_dd_account(request):
    client_id = request.GET.get('client_id')
    client_secret = request.GET.get('client_secret')

    if not client_id or not client_secret:
        return JsonResponse({
            "code": 400,
            "msg": "client_id and client_secret are required",
            "data": None
        })

    linked_account = (
        RobotIdMap.objects
        .filter(
            platform_robot_id=client_id,
            robot_secret=client_secret
        ).annotate(
            client_id=F('platform_robot_id'),
            client_secret=F('robot_secret'),
            robot_id=F('cybertron_robot_id'),
            robot_name=F('cybertron_robot_id__robot_name'),
            robot_creator=F('cybertron_robot_id__creator__username')
        )
        .values(
            'client_id',
            'client_secret',
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


# 解除钉钉账号绑定关系
@require_POST
@csrf_exempt
def del_dd_account(request):
    try:
        body = json.loads(request.body or "{}")
        robot_id = body.get("robot_id")
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

    is_exist = RobotIdMap.objects.filter(cybertron_robot_id=robot_id).exists()

    if not is_exist:
        return JsonResponse({
            "code": 0,
            "msg": "当前钉钉账号不存在绑定的agent！",
            "data": None
        })
    else:

        RobotIdMap.objects.filter(cybertron_robot_id=robot_id).delete()

        return JsonResponse({
            "code": 0,
            "msg": "解绑成功！",
            "data": None
        })
