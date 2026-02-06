import json

from django.db.models import F
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from apps.external_account.models import WecomInfo, RobotIdMap, WhatsappInfo


# 测试查询
@csrf_exempt
def test_function(request):
    print('请求成功！')
    return JsonResponse({
        "code": 200,
        "msg": "~~okk~~",
        "data": None
    })


# 查询企微账号是否绑定
@require_POST
@csrf_exempt
def query_wecom_account(request):
    try:
        body = json.loads(request.body or "{}")
        company_name = body.get("company_name")
        username = body.get("username")
    except json.decoder.JSONDecodeError:
        return JsonResponse({
            "code": 400,
            "msg": "参数异常！",
            "data": None
        })

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
        "code": 200,
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
            "code": 200,
            "msg": "当前企业微信账号不存在绑定的agent！",
            "data": None
        })
    else:

        WecomInfo.objects.filter(robot_id=robot_id).update(is_delete=1)

        return JsonResponse({
            "code": 200,
            "msg": "解绑成功！",
            "data": None
        })


# 查询钉钉账号是否绑定
@require_POST
@csrf_exempt
def query_dd_account(request):
    try:
        body = json.loads(request.body or "{}")
        client_id = body.get("client_id")
        client_secret = body.get("client_secret")
    except json.decoder.JSONDecodeError:
        return JsonResponse({
            "code": 400,
            "msg": "参数异常！",
            "data": None
        })

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
        "code": 200,
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
            "code": 200,
            "msg": "当前钉钉账号不存在绑定的agent！",
            "data": None
        })
    else:

        RobotIdMap.objects.filter(cybertron_robot_id=robot_id).delete()

        return JsonResponse({
            "code": 200,
            "msg": "解绑成功！",
            "data": None
        })


# 查询 whatsapp企业号 是否绑定
@require_POST
@csrf_exempt
def query_wa_account(request):
    try:
        body = json.loads(request.body or "{}")
        business_number = body.get("business_number")
        api_key = body.get("api_key")
    except json.decoder.JSONDecodeError:
        return JsonResponse({
            "code": 400,
            "msg": "参数异常！",
            "data": None
        })

    if not business_number or not api_key:
        return JsonResponse({
            "code": 400,
            "msg": "business_number and api_key are required",
            "data": None
        })

    linked_account = (
        WhatsappInfo.objects
        .filter(
            mobile=business_number,
            api_key=api_key,
            is_delete=0
        ).annotate(
            robot_name=F('robot__robot_name'),
            robot_creator=F('robot__creator__username')
        )
        .values(
            'mobile',
            'api_key',
            'robot_id',
            'robot_name',
            'robot_creator'
        )
    )

    query_result = {
        "code": 200,
        "msg": "success",
        "data": list(linked_account)
    }

    return JsonResponse(query_result)


# 解除 whatsapp企业号 绑定关系
@require_POST
@csrf_exempt
def del_wa_account(request):
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

    is_exist = WhatsappInfo.objects.filter(robot_id=robot_id, is_delete=0).exists()

    if not is_exist:
        return JsonResponse({
            "code": 200,
            "msg": "当前Whatsapp账号不存在绑定的agent！",
            "data": None
        })
    else:

        WhatsappInfo.objects.filter(robot_id=robot_id).update(is_delete=1)

        return JsonResponse({
            "code": 200,
            "msg": "解绑成功！",
            "data": None
        })
