# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WecomInfo(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='primary key')
    company_name = models.CharField(max_length=500, db_comment='企业名称')
    company_id = models.CharField(max_length=100, db_comment='企业id')
    username = models.CharField(max_length=150, db_comment='云机上登录的企微的账号名')
    user_id = models.CharField(max_length=100, db_comment='云机上登录的企微的账号ID')
    person_id = models.CharField(max_length=100, db_comment='云机上登录的企微的账号ID')
    corp_id = models.CharField(max_length=100, db_comment='企信通提供ID')
    robot_key = models.IntegerField(db_comment='机器人密钥')

    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, db_comment='最后修改时间')
    is_delete = models.IntegerField(db_comment='是否删除')

    robot = models.OneToOneField(
        'Robot',
        db_column='robot_id',  # 保持数据库字段名不变
        on_delete=models.DO_NOTHING,
        related_name='wecom_info'
    )

    class Meta:
        managed = False
        db_table = 'wecom_info'
        db_table_comment = '企业微信信息表'


class Robot(models.Model):
    id = models.BigAutoField(primary_key=True)
    robot_name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    welcome_message = models.TextField()
    tip_message = models.TextField()
    limit_message = models.TextField(blank=True, null=True)
    robot_tone = models.IntegerField(blank=True, null=True)
    robot_language = models.IntegerField(blank=True, null=True)
    initiative_reply = models.CharField(max_length=256, blank=True, null=True, db_comment='主动回复话术')
    plug_retrieval_status = models.IntegerField(blank=True, null=True, db_comment='插件调用状态')
    knowledge_retrieval_status = models.IntegerField(blank=True, null=True, db_comment='知识检索状态')
    minimum_threshold = models.IntegerField(blank=True, null=True, db_comment='相关度阈值')
    default_reply = models.CharField(max_length=256, blank=True, null=True, db_comment='兜里话术')
    manual_reply = models.BigIntegerField(blank=True, null=True, db_comment='转人工回复类型')
    divergence = models.FloatField()
    chat_model = models.CharField(max_length=50)
    max_context_num = models.IntegerField()
    reply_length = models.IntegerField(blank=True, null=True)
    max_reference_knowledge_num = models.IntegerField()
    correlation_threshold = models.IntegerField()
    creator = models.ForeignKey('Users', models.DO_NOTHING)
    # homeland = models.ForeignKey('Homeland', models.DO_NOTHING)
    is_guide_reading = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    secret_hashed = models.CharField(max_length=100, blank=True, null=True)
    prompt_template_id = models.IntegerField(blank=True, null=True, db_comment='提示词模板ID')
    emb_language = models.CharField(max_length=100, blank=True, null=True, db_comment='机器人语种')
    robot_code = models.CharField(max_length=128, blank=True, null=True, db_comment='机器人编码')
    is_synonym_replacement = models.IntegerField(blank=True, null=True, db_comment='是否同义词替换')
    is_keyword_answer = models.IntegerField(blank=True, null=True, db_comment='是否命中关键词')
    qa_answer_num = models.IntegerField(blank=True, null=True, db_comment='rag检索命中满足条数')
    qa_min_threshold = models.FloatField(blank=True, null=True, db_comment='qa命中最小相似度')
    is_qa_answer = models.IntegerField(blank=True, null=True, db_comment='是否命中qa回复')
    guiding_language = models.CharField(max_length=512, blank=True, null=True, db_comment='引导话术')
    is_manual_reply = models.IntegerField(blank=True, null=True, db_comment='是否开启人工回复')
    search_type = models.IntegerField(blank=True, null=True, db_comment='搜索类型')
    max_reference_folder_num = models.IntegerField(blank=True, null=True, db_comment='最大引用文件夹数')
    max_reference_single_folder_num = models.IntegerField(blank=True, null=True, db_comment='单文件夹引用最大引用知识数')
    max_tokens = models.IntegerField(blank=True, null=True, db_comment='模型对话最大tokens数')
    is_top_question = models.IntegerField(blank=True, null=True, db_comment='是否开启热门问题')
    question_optimization = models.IntegerField(blank=True, null=True, db_comment='是否开启问题只能优化')
    online_search = models.IntegerField(blank=True, null=True, db_comment='是否开启联网搜索')
    max_function_number = models.IntegerField(blank=True, null=True, db_comment='插件召回的最大方法数')
    min_function_threshold = models.IntegerField(blank=True, null=True, db_comment='插件召回最低相关度阈值')
    is_chatflow = models.IntegerField(blank=True, null=True, db_comment='是否开启对话流')
    is_start_intent = models.IntegerField(blank=True, null=True, db_comment='新会话是否从意图起始')
    intent_confidence = models.IntegerField(blank=True, null=True, db_comment='意图置信度')
    prioritize_intent_id = models.BigIntegerField(blank=True, null=True, db_comment='优先进入的意图id')
    is_high_light = models.IntegerField(blank=True, null=True, db_comment='是否开启高亮阈值')
    high_light_threshold = models.FloatField(blank=True, null=True, db_comment='高亮相关度阈值')
    is_output_risk = models.IntegerField(blank=True, null=True, db_comment='机器人输出是否开启风险检测')
    risk_requirements = models.TextField(blank=True, null=True, db_comment='风险拦截要求')
    is_long_term_memory_enable = models.IntegerField(blank=True, null=True, db_comment='机器人长期记忆配置')
    is_short_term_memory_enable = models.IntegerField(blank=True, null=True, db_comment='机器人短期记忆配置')
    voice_slang_words_enable = models.IntegerField(blank=True, null=True, db_comment='是否开启语言口水词')
    top_p = models.FloatField(db_comment='Top P')
    release_version = models.CharField(max_length=64, blank=True, null=True, db_comment='发布版本号')
    release_type = models.IntegerField(blank=True, null=True, db_comment='发布类型')
    copy_count = models.IntegerField(blank=True, null=True, db_comment='复制数')
    is_official = models.IntegerField(blank=True, null=True, db_comment='是否是官方')
    is_store = models.IntegerField(blank=True, null=True, db_comment='是否上架商店')
    tag_id = models.IntegerField(blank=True, null=True, db_comment='标签ID')
    release_time = models.DateTimeField(blank=True, null=True, db_comment='发布时间')
    release_user = models.BigIntegerField(blank=True, null=True, db_comment='发布人')
    access_config = models.TextField(blank=True, null=True, db_comment='访问配置')
    user_count = models.IntegerField(blank=True, null=True, db_comment='用户数')
    collect_count = models.IntegerField(blank=True, null=True, db_comment='收藏数')
    is_change = models.IntegerField(blank=True, null=True, db_comment='配置是否有变更')
    copying = models.IntegerField(blank=True, null=True, db_comment='是否正在复制')
    is_smart_suggestion = models.IntegerField(blank=True, null=True, db_comment='是否开启对话引导推荐')
    is_self_define_prompt = models.IntegerField(blank=True, null=True, db_comment='是否自定义对话引导推荐Prompt')
    smart_suggestion_prompt = models.TextField(blank=True, null=True, db_comment='对话引导Prompt')
    slang_type = models.IntegerField(blank=True, null=True, db_comment='智能口水词类型 1：通用 2：专用小模型 3：专用-prompt')
    slang_id = models.IntegerField(blank=True, null=True, db_comment='智能口水词ID')
    slang_prompt = models.CharField(max_length=2000, blank=True, null=True, db_comment='口水词prompt')
    db_search_correlation_threshold = models.FloatField()
    is_db_search = models.IntegerField(blank=True, null=True)
    max_db_serrch_number = models.IntegerField()
    sort_num = models.IntegerField(blank=True, null=True, db_comment='sort field')
    release_language = models.CharField(max_length=100, blank=True, null=True, db_comment='release_language')
    avatar_name = models.CharField(max_length=128, blank=True, null=True, db_comment='avatar name')
    avatar_color = models.CharField(max_length=128, blank=True, null=True, db_comment='avatar color')
    description = models.CharField(max_length=500, blank=True, null=True, db_comment='description')
    interaction_type = models.PositiveIntegerField(db_comment='Interaction type: 1-voice call, 0 as default')
    is_trigger = models.IntegerField(blank=True, null=True, db_comment='1 if robot has triggers, 0 otherwise')
    emb_model = models.CharField(max_length=200, blank=True, null=True, db_comment='emb_model')
    prioritize_flow_uuid = models.CharField(max_length=128, blank=True, null=True, db_comment='prioritize_flow_uuid')
    intent_embedding_model_name = models.CharField(max_length=128, blank=True, null=True, db_comment='intent_embedding_model_name')
    intent_embedding_language = models.CharField(max_length=128, blank=True, null=True, db_comment='intent_embedding_language')
    intent_embedding_rerank_enable = models.IntegerField(blank=True, null=True, db_comment='intent_embedding_rerank_enable')
    intent_embedding_rerank_model_name = models.CharField(max_length=128, blank=True, null=True, db_comment='intent_embedding_rerank_model_name')
    intent_rerank_confidence = models.IntegerField(blank=True, null=True, db_comment='intent_rerank_confidence (0-100, divide by 100 when using)')
    intent_embedding_llm_enable = models.IntegerField(blank=True, null=True, db_comment='intent_embedding_llm_enable')
    intent_embedding_llm_model_name = models.CharField(max_length=128, blank=True, null=True, db_comment='intent_embedding_llm_model_name')
    intent_embedding_llm_prompt = models.TextField(blank=True, null=True, db_comment='intent_embedding_llm_prompt')
    intent_embedding_llm_return_count = models.IntegerField(blank=True, null=True, db_comment='intent_embedding_llm_return_count')
    intent_final_llm_enable = models.IntegerField(blank=True, null=True, db_comment='intent_final_llm_enable')
    intent_final_llm_model_name = models.CharField(max_length=128, blank=True, null=True, db_comment='intent_final_llm_model_name')
    intent_final_llm_prompt = models.TextField(blank=True, null=True, db_comment='intent_final_llm_prompt')
    draft_saved_at = models.DateTimeField(blank=True, null=True)
    tenant_release_type = models.IntegerField(blank=True, null=True, db_comment='tenant_release_type 1: only use 2: can copy')
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'robot'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    is_delete = models.IntegerField()
    mobile = models.CharField(unique=True, max_length=128, blank=True, null=True, db_comment='手机号')
    avatar = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True, null=True, db_comment='nickname')
    need_bind_mobile = models.IntegerField(blank=True, null=True, db_comment='是否需要绑定手机号')
    user_type = models.IntegerField(blank=True, null=True, db_comment='用户类型')
    info = models.CharField(max_length=512, blank=True, null=True, db_comment='备注')
    operate_time = models.DateTimeField(blank=True, null=True, db_comment='管理操作时间')
    operate_user_id = models.BigIntegerField(blank=True, null=True, db_comment='操作者')
    expire_day = models.DateTimeField(blank=True, null=True, db_comment='expire day')
    days = models.IntegerField(blank=True, null=True, db_comment='days')
    is_permanent = models.IntegerField(blank=True, null=True, db_comment='is permanent')
    invite_token_id = models.IntegerField(blank=True, null=True, db_comment='invite token id')
    is_expire = models.IntegerField(blank=True, null=True, db_comment='账号是否过期')
    tenant_id = models.BigIntegerField(blank=True, null=True)
    tenant_user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
