import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (Windows)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 정의 (4단계 구분)
labels = ['상 (4.2점)', '중상 (3.9점)', '중하 (3.6점)', '하 (3.3점)']
scores = [4.2, 3.9, 3.6, 3.3]
# 단원별(1-3-3-1) * 3단원 = 총 빈도(3-9-9-3)
counts = [3, 9, 9, 3] 
colors = ['#f87171', '#fbbf24', '#60a5fa', '#34d399']  # Red, Amber, Blue, Green tones

# 1. 난이도별 문항 수 분포 (Bar Chart)
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, counts, color=colors)
plt.title('난이도별 문항 수 분포 (총 24문항)', fontsize=16)
plt.xlabel('난이도 (배점)', fontsize=12)
plt.ylabel('문항 수', fontsize=12)
plt.ylim(0, 10)

# 막대 위에 수치 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{int(height)}문항', ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig('item_distribution.png')
plt.close()

# 2. 총 배점 기여도 (Pie Chart)
# 각 난이도가 90점 만점에서 차지하는 비율 계산
total_scores = [s * c for s, c in zip(scores, counts)]

plt.figure(figsize=(8, 8))
plt.pie(total_scores, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=(0.05, 0.05, 0.05, 0.05))
plt.title('총 배점 기여도 (90점 만점)', fontsize=16)

plt.tight_layout()
plt.savefig('score_contribution.png')
plt.close()

print("Images updated with Korean labels: item_distribution.png, score_contribution.png")
