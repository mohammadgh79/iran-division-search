import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from locations.models import Division

# دیکشنری کدهای شهرستان‌ها
codes = {
    'تهران': '021',
    'مشهد': '051',
    'اصفهان': '031',
    'شیراز': '071',
    'تبریز': '041',
    'کرج': '026',
    'قم': '025',
    'رشت': '013',
    'زنجان': '024',
    'کرمانشاه': '083',
    'اهواز': '061',
    'ارومیه': '044',
    'یزد': '035',
    'بندرعباس': '076',
    'سنندج': '087',
    'همدان': '081',
    'اراک': '086',
    'بوشهر': '077',
    'ایلام': '084',
    'خرم‌آباد': '066',
    'ساری': '011',
    'گرگان': '017',
    'شهرکرد': '038',
    'بیرجند': '056',
    'بجنورد': '058',
    'قزوین': '028',
    'سمنان': '023',
    'زاهدان': '054',
    'کرمان': '034',
    'یاسوج': '074',
}

print("🔄 در حال بررسی...")
print(f"تعداد کل رکوردها: {Division.objects.count()}")

# اول ببینیم تهران توی دیتابیس هست یا نه
try:
    tehran = Division.objects.filter(name__icontains='تهران')
    print(f"تعداد موارد پیدا شده برای تهران: {tehran.count()}")
    for t in tehran:
        print(f"ID: {t.id}, Name: {t.name}, Parent: {t.parent}, Code: {t.code}")
except Exception as e:
    print(f"خطا: {e}")

print("\n🔄 در حال اضافه کردن کدها...")
for name, code in codes.items():
    try:
        # جستجو با نام دقیق
        division = Division.objects.get(name=name)
        division.code = code
        division.save()
        print(f"✅ {name} ← کد {code} اضافه شد")
    except Division.DoesNotExist:
        print(f"❌ {name} پیدا نشد!")
    except Division.MultipleObjectsReturned:
        print(f"⚠️ چند تا {name} وجود داره!")