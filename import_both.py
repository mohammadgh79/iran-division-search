import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from locations.models import Division

def import_file1():
    print("📂 در حال وارد کردن فایل اول (MJavadSF)...")
    with open('iran_data1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        province_name = item.get('province-fa') or item.get('province')
        if province_name:
            province, _ = Division.objects.get_or_create(name=province_name)
            print(f"✅ استان: {province_name}")
            
            cities = item.get('cities', [])
            for city in cities:
                city_name = city.get('city-fa') or city.get('city')
                if city_name:
                    Division.objects.get_or_create(name=city_name, parent=province)
                    print(f"   📍 شهر: {city_name}")
    print("✅ فایل اول کامل شد.\n")

def import_file2():
    print("📂 در حال وارد کردن فایل دوم (tafakoritech)...")
    with open('iran_data2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # دیکشنری برای نگهداری استان‌ها
    provinces = {}
    
    # اول استان‌ها رو اضافه کن
    for item in data:
        if item.get('type') == 'province':
            p = Division.objects.get_or_create(name=item['name'])[0]
            provinces[item['id']] = p
            print(f"✅ استان: {item['name']}")
    
    # بعد شهرها رو اضافه کن
    for item in data:
        if item.get('type') == 'city':
            province_id = item.get('province_id')
            if province_id and province_id in provinces:
                Division.objects.get_or_create(
                    name=item['name'], 
                    parent=provinces[province_id]
                )
                print(f"   📍 شهر: {item['name']}")
    
    print("✅ فایل دوم کامل شد.\n")

if __name__ == '__main__':
    print("🚀 شروع وارد کردن دیتا از دو فایل...")
    Division.objects.all().delete()
    print("🗑️ دیتای قبلی پاک شد.\n")
    
    import_file1()
    import_file2()
    
    total = Division.objects.count()
    print(f"\n🎉 مجموعاً {total} رکورد وارد شد.")