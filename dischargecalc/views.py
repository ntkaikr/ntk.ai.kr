from django.shortcuts import render
from datetime import date, timedelta

def index(request):
    return render(request, 'dischargecalc/index.html', {
        'today': date.today().isoformat()
    })

def result(request):
    if request.method == 'POST':
        enlist_date_str = request.POST.get('enlist_date', '').strip()
        military_branch = request.POST.get('military_branch', '').strip()
        service_type = request.POST.get('service_type', '').strip()
        rank_type = request.POST.get('rank_type', '').strip()

        try:
            # ✅ 유효성 검사: 장교/부사관은 현역만 가능
            if rank_type in ['장교', '부사관'] and service_type != '현역':
                return render(request, 'dischargecalc/index.html', {
                    'error': '장교/부사관은 반드시 "현역" 복무 형태로만 선택 가능합니다.',
                    'today': date.today().isoformat()
                })

            # ✅ 유효성 검사: 비현역 복무는 병사만 가능
            if service_type in ['상근예비역', '사회복무요원', '전문연구요원'] and rank_type != '병사':
                return render(request, 'dischargecalc/index.html', {
                    'error': f'"{service_type}"은(는) 병사 계급에서만 선택할 수 있습니다.',
                    'today': date.today().isoformat()
                })

            # 날짜 파싱
            y, m, d = map(int, enlist_date_str.split('-'))
            enlist_date = date(y, m, d)

            # 복무개월 계산
            service_months = get_service_months(military_branch, service_type, rank_type)

            # 전역일 계산 (간단히 30일 × 개월)
            discharge_date = enlist_date + timedelta(days=service_months * 30)

            today = date.today()
            d_day = (discharge_date - today).days

            # 예비군 및 민방위 계산
            reservist_start_year = discharge_date.year + 1
            reservist_end_year = reservist_start_year + 5
            civil_defense_start_year = reservist_end_year + 1

            return render(request, 'dischargecalc/result.html', {
                'enlist_date': enlist_date,
                'discharge_date': discharge_date,
                'd_day': d_day,
                'reservist_start_year': reservist_start_year,
                'reservist_end_year': reservist_end_year,
                'civil_defense_start_year': civil_defense_start_year,
                'military_branch': military_branch,
                'service_type': service_type,
                'rank_type': rank_type,
            })

        except:
            return render(request, 'dischargecalc/index.html', {
                'error': '입력값을 확인해주세요.',
                'today': date.today().isoformat()
            })

def get_service_months(military_branch, service_type, rank_type):
    # 부사관/장교는 무조건 36개월
    if rank_type == '장교':
        return 36
    elif rank_type == '부사관':
        return 36

    # 병사 + 복무형태별 세팅
    if service_type == '상근예비역':
        return 18
    elif service_type == '사회복무요원':
        return 21
    elif service_type == '전문연구요원':
        return 36
    elif service_type == '현역':
        if military_branch == '육군':
            return 18
        elif military_branch == '해병대':
            return 18
        elif military_branch == '해군':
            return 20
        elif military_branch == '공군':
            return 21
        else:
            return 18  # 기타는 육군 기준
    else:
        return 18  # 기본값
