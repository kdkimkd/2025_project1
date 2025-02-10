import random
import json

# 단어 데이터 불러오기
with open("words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

# 단어 리스트 생성
word_list = list(words.keys())

# 점수 초기화
score = 0
num_questions = 5  # 문제 개수 설정

print("🔤 영어 단어 퀴즈 게임을 시작합니다! 🔤")
print("="*40)

for i in range(num_questions):
    word = random.choice(word_list)  # 랜덤 단어 선택
    answer = input(f"Q{i+1}. '{word}'의 뜻은? ")

    if answer.strip() == words[word]:  # 정답 확인
        print("✅ 정답입니다!")
        score += 1
    else:
        print(f"❌ 오답! 정답은 '{words[word]}' 입니다.")

print("="*40)
print(f"🎯 최종 점수: {score} / {num_questions}")
