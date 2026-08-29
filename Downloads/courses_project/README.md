# منصة الكورسات الأونلاين - Django

## خطوات التشغيل

```bash
# 1. إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate   # على ويندوز: venv\Scripts\activate

# 2. تثبيت المتطلبات
pip install -r requirements.txt

# 3. إنشاء ملفات الترحيل (migrations)
python manage.py makemigrations

# 4. تطبيق الترحيل على قاعدة البيانات
python manage.py migrate

# 5. إنشاء حساب الأدمن تلقائياً (admin / admin123 للتطوير المحلي فقط)
python manage.py create_default_superuser

# 6. تشغيل السيرفر
python manage.py runserver
```

بعدها افتح المتصفح على:
- الموقع: http://127.0.0.1:8000/
- لوحة التحكم: http://127.0.0.1:8000/admin/  (المستخدم: admin | كلمة المرور: admin123)

## تنبيه أمني مهم
بيانات الدخول admin/admin123 مخصصة **للتطوير المحلي فقط** على جهازك.
قبل نشر المشروع على أي سيرفر متاح على الإنترنت:
1. غيّر كلمة المرور فوراً من لوحة التحكم أو عبر:
   `python manage.py changepassword admin`
2. غيّر `SECRET_KEY` في settings.py.
3. اجعل `DEBUG = False`.
4. حدّث `ALLOWED_HOSTS` و `CSRF_TRUSTED_ORIGINS` بدومينك الحقيقي مع HTTPS.
