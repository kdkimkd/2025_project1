import random
import json
import tkinter as tk
from tkinter import messagebox

# 단어 데이터 불러오기
with open("words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

word_list = list(words.keys())  # 단어 리스트
current_word = None  # 현재 문제 단어
score = 0  # 점수
num_questions = 5  # 총 문제 수
question_count = 0  # 현재 문제 수

# 게임 초기 설정
def next_question():
    global current_word, question_count
    if question_count < num_questions:
        question_count += 1
        current_word = random.choice(word_list)  # 랜덤 단어 선택
        lbl_question.config(text=f"Q{question_count}. '{current_word}'의 뜻은?")
        entry_answer.delete(0, tk.END)  # 입력창 초기화
    else:
        messagebox.showinfo("게임 종료", f"🎯 최종 점수: {score} / {num_questions}")
        window.quit()

# 정답 확인
def check_answer():
    global score
    answer = entry_answer.get().strip()
    if answer == words[current_word]:
        messagebox.showinfo("정답!", "✅ 정답입니다!")
        score += 1
    else:
        messagebox.showinfo("오답!", f"❌ 오답! 정답은 '{words[current_word]}' 입니다.")
    next_question()

# Tkinter 윈도우 설정
window = tk.Tk()
window.title("영어 단어 퀴즈 게임")
window.geometry("400x250")

# 문제 표시 레이블
lbl_question = tk.Label(window, text="", font=("Arial", 14))
lbl_question.pack(pady=20)

# 정답 입력 필드
entry_answer = tk.Entry(window, font=("Arial", 12))
entry_answer.pack(pady=10)

# 정답 확인 버튼
btn_check = tk.Button(window, text="정답 제출", font=("Arial", 12), command=check_answer)
btn_check.pack(pady=10)

# 시작할 때 첫 문제 출제
next_question()

# Tkinter 실행
window.mainloop()
