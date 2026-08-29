"""
إعدادات مشروع Django لموقع الكورسات الأونلاين
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# =======================
# إعدادات الأمان الأساسية
# =======================
# ملاحظة: غيّر هذا المفتاح في بيئة الإنتاج ولا تتركه كما هو
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-CHANGE-THIS-KEY-BEFORE-PRODUCTION"
)

# اجعلها False في بيئة الإنتاج
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
# أضف نطاقك هنا عند النشر، مثال:
# ALLOWED_HOSTS = ["127.0.0.1", "localhost", "example.com", "www.example.com"]

# =======================
# التطبيقات المثبتة
# =======================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "courses",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# =======================
# إعدادات القوالب (Templates)
# مهمة لعمل لوحة تحكم الأدمن بدون أخطاء
# =======================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# =======================
# قاعدة البيانات (SQLite للتطوير)
# =======================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =======================
# التحقق من كلمات المرور
# =======================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =======================
# اللغة والمنطقة الزمنية
# =======================
LANGUAGE_CODE = "en"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_TZ = True

# =======================
# الملفات الثابتة والوسائط
# =======================
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =======================
# إعدادات CSRF
# =======================
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]
# عند النشر على دومين حقيقي بـ HTTPS أضف رابطه هنا، مثال:
# CSRF_TRUSTED_ORIGINS = ["https://example.com"]

CSRF_COOKIE_SECURE = False  # اجعلها True عند استخدام HTTPS في الإنتاج
SESSION_COOKIE_SECURE = False  # اجعلها True عند استخدام HTTPS في الإنتاج

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
