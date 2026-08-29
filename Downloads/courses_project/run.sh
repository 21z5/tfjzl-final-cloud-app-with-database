#!/bin/bash
# سكريبت تشغيل تلقائي لمشروع الكورسات - لينكس / ماك
# شغّله بالأمر: bash run.sh

set -e
cd "$(dirname "$0")"

echo "==> إنشاء البيئة الافتراضية (إن لم تكن موجودة)..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

echo "==> تثبيت المتطلبات..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo "==> تجهيز قاعدة البيانات..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "==> إنشاء حساب الأدمن (admin / admin123) إن لم يكن موجوداً..."
python manage.py create_default_superuser

echo "==> تشغيل السيرفر..."
echo "افتح المتصفح على: http://127.0.0.1:8000/"
echo "لوحة التحكم: http://127.0.0.1:8000/admin/  (admin / admin123)"
python manage.py runserver
