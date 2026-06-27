# جستجوی تقسیمات کشوری ایران 🇮🇷

یک پروژه با فریمورک جنگو برای جستجوی استانها وشهرستان ها وروستاهای ایران با قابلیت جسنجو براساس کد تلفن ثابت
---

##  قابلیت‌ها

- جستجوی استان، شهرستان و روستا با نام
- جستجو بر اساس کد تلفن ثابت
- نمایش اطلاعات استان، شهرستان و روستا
- نمایش سلسله‌مراتب (استان ← شهرستان ← روستا)
- پنل مدیریت Django برای مدیریت داده‌ها
- API ساده برای جستجو
- رابط کاربری ساده و سریع

---

##  تکنولوژی‌های استفاده‌شده

- Python 3.14
- Django 6.0.6
- SQLite (Development)
- PostgreSQL (Production)
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Git

---

##  پیش‌ نیازها

- Python 3.14 یا بالاتر
- Git
- pip

---

##  نصب و اجرا

1.###  کلون کردن پروژه

```bash
git clone https://git.risq.ir/USERNAME/iran-division-search.git
cd iran-division-search
```

2.###  ساخت محیط مجازی

```bash
python -m venv .venv
```

3.###  فعال کردن محیط مجازی

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

4.###  نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

5.###  اعمال Migrationها

```bash
python manage.py migrate
```

6.###  اجرای پروژه

```bash
python manage.py runserver
```

سپس مرورگر را باز کنید:

```
http://127.0.0.1:8000/
```

---

##  ساختار پروژه

```
iran-division-search/
│
├── accounts/
├── search/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---



##  API

نمونه درخواست:

```
GET /api/search/?q=تهران
```

نمونه پاسخ:

```json
{
    "province": "تهران",
    "city": "تهران",
    "village": null
}
```

---





## توسعه‌دهنده

**Mohammad Ghasemi**