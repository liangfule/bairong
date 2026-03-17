from django.apps import AppConfig


class TodoListConfig(AppConfig):
    name = 'apps.todo_list'

    def ready(self):
        # 避免在 runserver 时重复启动（Django 会加载两次）
        import os
        if os.environ.get('RUN_MAIN') == 'true':
            from apscheduler.schedulers.background import BackgroundScheduler
            from apps.todo_list.views import daily_task
            scheduler = BackgroundScheduler()
            # 每天 09:45 执行
            # scheduler.add_job(daily_task, 'cron', hour=9, minute=45)
            scheduler.add_job(daily_task, 'interval', seconds=10)
            scheduler.start()