from django.shortcuts import render
from django.http import JsonResponse
from .models import Division
from django.db.models import Q
import sys
import os

# اضافه کردن مسیر پروژه به سیستم
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from iran_codes import search_by_code_or_name, search_by_phone_code
except ImportError:
    # اگر فایل وجود نداشت، توابع خالی تعریف می‌شوند
    def search_by_code_or_name(query):
        return []
    def search_by_phone_code(code):
        return []

def home(request):
    return render(request, 'search.html')

def search_api(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return JsonResponse({'error': 'متن جستجو را وارد کنید'}, status=400)
    
    results = []
    
    # 1. جستجو در دیتابیس
    db_results = Division.objects.filter(
        Q(name__icontains=query) | Q(code__icontains=query)
    )
    
    for r in db_results:
        results.append({
            'name': r.name,
            'parent': r.parent.name if r.parent else None,
            'code': r.code or '',
            'source': 'database'
        })
    
    # 2. جستجو در کدها (اگر query عددی باشد یا در کدها باشد)
    if query.isdigit() or len(query) >= 2:
        code_results = search_by_code_or_name(query)
        for r in code_results:
            # جلوگیری از تکراری بودن نتایج
            if not any(item['name'] == r['name'] for item in results):
                results.append({
                    'name': r['name'],
                    'parent': r['parent'],
                    'code': r['code'],
                    'source': 'phone_code'
                })
    
    # مرتب‌سازی نتایج
    results = sorted(results, key=lambda x: x['name'])
    
    return JsonResponse({'results': results, 'count': len(results)})

def get_by_code(request):
    code = request.GET.get('code', '').strip()
    if not code:
        return JsonResponse({'error': 'کد را وارد کنید'}, status=400)
    
    results = []
    
    # 1. جستجو در دیتابیس
    db_results = Division.objects.filter(
        Q(code__icontains=code) | Q(name__icontains=code)
    )
    
    for r in db_results:
        results.append({
            'name': r.name,
            'parent': r.parent.name if r.parent else None,
            'code': r.code or '',
            'source': 'database'
        })
    
    # 2. جستجو در کدهای تلفن
    if code.isdigit():
        phone_results = search_by_phone_code(code)
        for r in phone_results:
            if not any(item['name'] == r['name'] for item in results):
                results.append({
                    'name': r['name'],
                    'parent': r['parent'],
                    'code': r['code'],
                    'source': 'phone_code'
                })
    
    if results:
        return JsonResponse({'results': results, 'count': len(results)})
    else:
        return JsonResponse({'error': 'یافت نشد'}, status=404)