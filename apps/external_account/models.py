# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#钉钉
class RobotIdMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_robot_id = models.CharField(unique=True, max_length=200, blank=True, null=True)
    cybertron_robot_id = models.ForeignKey('Robot', models.DO_NOTHING)
    robot_secret = models.CharField(max_length=128, blank=True, null=True)
    enable_group_chat = models.IntegerField(blank=True, null=True)
    use_card = models.IntegerField()
    robot_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'robot_id_map'

#企业微信
class WecomInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=500)
    company_id = models.CharField(max_length=100)
    username = models.CharField(max_length=150)
    user_id = models.CharField(max_length=100)
    person_id = models.CharField(max_length=100)
    corp_id = models.CharField(max_length=100)
    robot_key = models.IntegerField()

    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField()

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

# Whatsapp
class WhatsappInfo(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='primary key')
    mobile = models.CharField(max_length=500, db_comment='手机号')
    api_key = models.CharField(max_length=100, db_comment='api_key')
    robot_key = models.IntegerField(db_comment='机器人密钥')

    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(blank=True, null=True, db_comment='最后修改时间')
    is_delete = models.IntegerField(db_comment='是否删除')
    agent_type = models.IntegerField()

    robot = models.OneToOneField(
        'Robot',
        db_column='robot_id',  # 保持数据库字段名不变
        on_delete=models.DO_NOTHING,
        related_name='whatsapp_info'
    )

    class Meta:
        managed = False
        db_table = 'whatsapp_info'
        db_table_comment = 'whatsapp信息表'

#Robot
class Robot(models.Model):
    id = models.BigAutoField(primary_key=True)
    robot_name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    welcome_message = models.TextField()
    tip_message = models.TextField()
    limit_message = models.TextField(blank=True, null=True)
    robot_tone = models.IntegerField(blank=True, null=True)
    robot_language = models.IntegerField(blank=True, null=True)
    initiative_reply = models.CharField(max_length=256, blank=True, null=True)
    plug_retrieval_status = models.IntegerField(blank=True, null=True)
    knowledge_retrieval_status = models.IntegerField(blank=True, null=True)
    minimum_threshold = models.IntegerField(blank=True, null=True)
    default_reply = models.CharField(max_length=256, blank=True, null=True)
    manual_reply = models.BigIntegerField(blank=True, null=True)
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
    prompt_template_id = models.IntegerField(blank=True, null=True)
    emb_language = models.CharField(max_length=100, blank=True, null=True)
    robot_code = models.CharField(max_length=128, blank=True, null=True)
    is_synonym_replacement = models.IntegerField(blank=True, null=True)
    is_keyword_answer = models.IntegerField(blank=True, null=True)
    qa_answer_num = models.IntegerField(blank=True, null=True)
    qa_min_threshold = models.FloatField(blank=True, null=True)
    is_qa_answer = models.IntegerField(blank=True, null=True,)
    guiding_language = models.CharField(max_length=512, blank=True, null=True)
    is_manual_reply = models.IntegerField(blank=True, null=True)
    search_type = models.IntegerField(blank=True, null=True)
    max_reference_folder_num = models.IntegerField(blank=True, null=True)
    max_reference_single_folder_num = models.IntegerField(blank=True, null=True)
    max_tokens = models.IntegerField(blank=True, null=True)
    is_top_question = models.IntegerField(blank=True, null=True)
    question_optimization = models.IntegerField(blank=True, null=True)
    online_search = models.IntegerField(blank=True, null=True)
    max_function_number = models.IntegerField(blank=True, null=True)
    min_function_threshold = models.IntegerField(blank=True, null=True)
    is_chatflow = models.IntegerField(blank=True, null=True)
    is_start_intent = models.IntegerField(blank=True, null=True)
    intent_confidence = models.IntegerField(blank=True, null=True)
    prioritize_intent_id = models.BigIntegerField(blank=True, null=True)
    is_high_light = models.IntegerField(blank=True, null=True)
    high_light_threshold = models.FloatField(blank=True, null=True)
    is_output_risk = models.IntegerField(blank=True, null=True)
    risk_requirements = models.TextField(blank=True, null=True)
    is_long_term_memory_enable = models.IntegerField(blank=True, null=True)
    is_short_term_memory_enable = models.IntegerField(blank=True, null=True)
    voice_slang_words_enable = models.IntegerField(blank=True, null=True)
    top_p = models.FloatField()
    release_version = models.CharField(max_length=64, blank=True, null=True)
    release_type = models.IntegerField(blank=True, null=True)
    copy_count = models.IntegerField(blank=True, null=True)
    is_official = models.IntegerField(blank=True, null=True)
    is_store = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    release_time = models.DateTimeField(blank=True, null=True)
    release_user = models.BigIntegerField(blank=True, null=True)
    access_config = models.TextField(blank=True, null=True)
    user_count = models.IntegerField(blank=True, null=True)
    collect_count = models.IntegerField(blank=True, null=True)
    is_change = models.IntegerField(blank=True, null=True)
    copying = models.IntegerField(blank=True, null=True)
    is_smart_suggestion = models.IntegerField(blank=True, null=True)
    is_self_define_prompt = models.IntegerField(blank=True, null=True)
    smart_suggestion_prompt = models.TextField(blank=True, null=True)
    slang_type = models.IntegerField(blank=True, null=True)
    slang_id = models.IntegerField(blank=True, null=True)
    slang_prompt = models.CharField(max_length=2000, blank=True, null=True)
    db_search_correlation_threshold = models.FloatField()
    is_db_search = models.IntegerField(blank=True, null=True)
    max_db_serrch_number = models.IntegerField()
    sort_num = models.IntegerField(blank=True, null=True)
    release_language = models.CharField(max_length=100, blank=True, null=True)
    avatar_name = models.CharField(max_length=128, blank=True, null=True)
    avatar_color = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    interaction_type = models.PositiveIntegerField()
    is_trigger = models.IntegerField(blank=True, null=True)
    emb_model = models.CharField(max_length=200, blank=True, null=True)
    prioritize_flow_uuid = models.CharField(max_length=128, blank=True, null=True)
    intent_embedding_model_name = models.CharField(max_length=128, blank=True, null=True)
    intent_embedding_language = models.CharField(max_length=128, blank=True, null=True)
    intent_embedding_rerank_enable = models.IntegerField(blank=True, null=True)
    intent_embedding_rerank_model_name = models.CharField(max_length=128, blank=True, null=True)
    intent_rerank_confidence = models.IntegerField(blank=True, null=True)
    intent_embedding_llm_enable = models.IntegerField(blank=True, null=True)
    intent_embedding_llm_model_name = models.CharField(max_length=128, blank=True, null=True)
    intent_embedding_llm_prompt = models.TextField(blank=True, null=True)
    intent_embedding_llm_return_count = models.IntegerField(blank=True, null=True)
    intent_final_llm_enable = models.IntegerField(blank=True, null=True)
    intent_final_llm_model_name = models.CharField(max_length=128, blank=True, null=True)
    intent_final_llm_prompt = models.TextField(blank=True, null=True)
    draft_saved_at = models.DateTimeField(blank=True, null=True)
    tenant_release_type = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'robot'

#用户
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
    mobile = models.CharField(unique=True, max_length=128, blank=True, null=True)
    avatar = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    need_bind_mobile = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=512, blank=True, null=True)
    operate_time = models.DateTimeField(blank=True, null=True)
    operate_user_id = models.BigIntegerField(blank=True, null=True)
    expire_day = models.DateTimeField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    is_permanent = models.IntegerField(blank=True, null=True)
    invite_token_id = models.IntegerField(blank=True, null=True)
    is_expire = models.IntegerField(blank=True, null=True)
    tenant_id = models.BigIntegerField(blank=True, null=True)
    tenant_user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
