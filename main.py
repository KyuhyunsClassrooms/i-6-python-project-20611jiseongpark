def input_single_user():
    """
    [함수 1] 한 사람의 정보를 입력받아 2차원 리스트로 저장 후 반환하는 함수
    """
    print("\n" + "=" * 50)
    print("         [ BMI 기반 체지방률 계산기 ]")
    print("=" * 50)
    print("※ 주의: 나이, 키, 몸무게는 '숫자만' 입력해 주세요. (예: 175, 65)\n")
    
    name = input("▶ 이름 입력: ").strip()
    gender = input("▶ 성별 입력 (남성/여성): ").strip()
    
    # 성별 입력 검증
    if gender not in ["남성", "여성"]:
        print("\n[오류] 성별은 '남성' 또는 '여성'으로만 입력해야 합니다.")
        return []
        
    try:
        age = int(input("▶ 나이 입력 (세): "))
        height = float(input("▶ 신장 입력 (cm): "))
        weight = float(input("▶ 체중 입력 (kg): "))
    except ValueError:
        print("\n" + "!" * 50)
        print("[입력 오류] 키, 몸무게, 나이에 문자(cm, kg 등)가 포함되었습니다.")
        print("반드시 '숫자만' 입력하셔야 계산이 가능합니다.")
        print("!" * 50)
        return []

    # 조건을 충족하기 위해 1명의 데이터도 2차원 리스트 [[...]] 구조로 생성
    single_user_matrix = [[name, gender, age, height, weight]]
    return single_user_matrix


def calculate_metrics(bmi, age, gender):
    """
    [함수 2] BMI와 개인 정보를 기반으로 체지방률을 연산하는 함수
    """
    if gender == "남성":
        gender_constant = 1
    else:
        gender_constant = 0
        
    # 학술 공식(Deurenberg) 기반 체지방률 계산
    body_fat = (1.20 * bmi) + (0.23 * age) - (10.8 * gender_constant) - 5.4
    return round(body_fat, 2)


def recommend_exercise(gender):
    """
    [함수 4 - 추가됨] 체지방 관리가 필요한 사용자를 위한 성별 맞춤형 운동 추천 함수
    """
    print("\n💡 [추천 건강 가이드]")
    if gender == "남성":
        print("  -> 대근육 중심의 웨이트 트레이닝과 고강도 인터벌 트레이닝(HIIT)을 추천합니다.")
        print("  -> 추천 루틴: 스쿼트/데드리프트(근력 유지) + 인터벌 러닝 30분(체지방 연소)")
    else:
        print("  -> 신체 탄력과 코어 강화를 위한 근력 운동 및 전신 유산소 운동을 추천합니다.")
        print("  -> 추천 루틴: 플랭크/런지(코어 및 하체) + 빠른 걷기 또는 수영 40분(체지방 연소)")
    print("  -> 팁: 주 3~4회 규칙적인 운동과 함께 단백질 위주의 식단을 병행해 보세요!")


def process_and_print_result(user_data):
    """
    [함수 3] 2차원 리스트 데이터를 전달받아 연산 및 체지방률 판정 결과를 출력하는 함수
    """
    if not user_data:
        return

    # 반복문(for)을 사용하여 2차원 리스트 내부의 데이터 추출
    for row in user_data:
        name = row[0]
        gender = row[1]
        age = row[2]
        height = row[3]
        weight = row[4]
        
        # BMI 계산
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)
        
        # 체지방률 계산 함수 호출
        body_fat = calculate_metrics(bmi, age, gender)
        
        # 성별 체지방률 기준에 따른 과체중 판정 및 플래그 설정
        need_management = False
        if gender == "남성":
            if body_fat >= 20.0:
                status = "체지방 관리 필요 (과체중 위험)"
                need_management = True
            else:
                status = "정상 범위"
        else:  # 여성인 경우
            if body_fat >= 28.0:
                status = "체지방 관리 필요 (과체중 위험)"
                need_management = True
            else:
                status = "정상 범위"
        
        # 결과 출력
        print("\n" + "=" * 50)
        print(f"  [{name}님의 건강 정보 분석 결과]")
        print("-" * 50)
        print(f"  - 성별 / 나이 : {gender} / {age}세")
        print(f"  - 신장 / 체중 : {height}cm / {weight}kg")
        print(f"  - BMI 지수   : {bmi}")
        print(f"  - 예상 체지방률: {body_fat}%")
        print(f"  - 체지방 판정 : {status}")
        print("=" * 50)
        
        # 관리 필요 판정이 나왔을 때만 운동 추천 함수(함수 4)를 호출
        if need_management:
            recommend_exercise(gender)
            print("=" * 50)


# --- 프로그램 실행 메인 루틴 ---
if __name__ == "__main__":
    while True:
        # 1. 정보 입력
        user_matrix = input_single_user()
        
        # 2. 연산 및 결과 화면 출력 (과체중 시 운동 추천 포함)
        process_and_print_result(user_matrix)
        
        # 3. 한글 '예 / 아니요' 재실행 확인
        print("\n" + "-" * 50)
        retry = input("▶ 새로운 사람의 정보를 입력하시겠습니까? (예 / 아니요): ").strip()
        
        if retry in ['예', '네']:
            print("\n새로운 입력을 시작합니다...")
            continue
        else:
            print("\n계산기를 종료합니다. 이용해 주셔서 감사합니다!")
            print("-" * 50)
            input("\n[엔터(Enter)]를 누르면 창이 완전히 닫힙니다.")
            break