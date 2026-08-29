import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    ينشئ حساب سوبر يوزر تلقائياً إذا لم يكن موجوداً، لتسهيل الدخول على
    لوحة التحكم أثناء التطوير المحلي فقط.

    القيم الافتراضية (admin / admin123) مخصصة للتطوير على جهازك فقط.
    يمكن تغييرها عبر متغيرات البيئة DJANGO_SUPERUSER_USERNAME و
    DJANGO_SUPERUSER_PASSWORD و DJANGO_SUPERUSER_EMAIL بدل تعديل الكود.

    تحذير: لا تستخدم هذه البيانات الافتراضية في بيئة إنتاج (production)
    أو أي سيرفر متاح على الإنترنت.
    """

    help = "ينشئ سوبر يوزر افتراضي للتطوير المحلي إذا لم يكن موجوداً"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"المستخدم '{username}' موجود مسبقاً، تم تخطي الإنشاء."))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"تم إنشاء سوبر يوزر: {username} / {password}"))
        self.stdout.write(self.style.WARNING("تذكير: غيّر كلمة المرور فوراً إذا كان المشروع سيُنشر على الإنترنت."))
