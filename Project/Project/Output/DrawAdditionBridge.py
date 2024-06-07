import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 또는 'AppleGothic' for macOS
plt.rcParams['axes.unicode_minus'] = False

def draw_addition_bridge_and_forces(forces, stresses, height, num_panels):
    # 각도 a = np.arctan(2)
    a = np.arctan(2)

    # 이등변 삼각형의 크기
    base_length = 10
    height = base_length / 2 * np.tan(a)

    # 위 꼭지점 좌표 저장할 리스트
    apex_points = []

    plt.figure(figsize=(14, 14))  # 그래프 크기를 더 크게 설정
    plt.axhline(0, color='grey', linewidth=0.5)

    for i in range(num_panels):
        # 기준점 계산
        base_x = i * base_length
        base_y = 0

        # 이등변 삼각형의 꼭지점 계산
        left_x = base_x
        left_y = base_y
        right_x = base_x + base_length
        right_y = base_y
        apex_x = base_x + base_length / 2
        apex_y = base_y + height
        apex_points.append((apex_x, apex_y))

        # 이등변 삼각형 그리기
        triangle_x = [left_x, apex_x, right_x, left_x]
        triangle_y = [left_y, apex_y, right_y, left_y]
        plt.plot(triangle_x, triangle_y, 'b-')

        # 시작점과 끝점 표시 (투명도 조절)
        if i == 0:
            plt.plot(left_x, left_y, 'r^', markersize=10, alpha=0.7, markerfacecolor='r', markeredgewidth=0)
        elif i == num_panels - 1:
            plt.plot(right_x, right_y, 'ro', markersize=10, alpha=0.7, markerfacecolor='r', markeredgewidth=0)

    # 위 꼭지점들을 직선으로 연결
    apex_x_points, apex_y_points = zip(*apex_points)
    plt.plot(apex_x_points, apex_y_points, 'b-')

    # 그래프 제목 설정
    plt.title('추가 교량')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # 부재력과 응력 표를 아래에 가운데 정렬하여 표시
    column_labels = ["Member", "Force (kN)", "Stress (N/mm^2)"]
    cell_text = []

    # 부재력 번호가 F1부터 F4*num_panels - 1까지 생성되도록 리스트를 생성
    for i in range(1, 4 * num_panels):
        cell_text.append([f"F{i}", f"{forces[i-1]:.2f}", f"{stresses[i-1]:.2f}"])

    plt.subplots_adjust(bottom=0.4)
    ax = plt.gca()
    table = plt.table(cellText=cell_text, colLabels=column_labels, cellLoc='center', loc='bottom', colWidths=[0.2, 0.2, 0.2], bbox=[0.1, -2.5, 0.8, 2.3])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(2, 2)

    plt.show()
