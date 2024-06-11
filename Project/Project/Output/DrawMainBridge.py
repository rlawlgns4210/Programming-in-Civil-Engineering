
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import matplotlib.patches as patches

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 또는 'AppleGothic' for macOS
plt.rcParams['axes.unicode_minus'] = False
def draw_bridge_and_forces(forces, stresses, height):
    # 각도 a = np.arctan(2)
    a = np.arctan(2)

    # 이등변 삼각형의 개수
    n = 6

    # 이등변 삼각형의 크기
    base_length = 10
    height = base_length / 2 * np.tan(a)

    # 위 꼭지점 좌표 저장할 리스트
    apex_points = []

    plt.figure(figsize=(14, 14))  # 그래프 크기를 더 크게 설정

    for i in range(n):
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

        # 치수선 추가 (개별 삼각형)
        if i == 0:
            # 높이 치수선 (맨 왼쪽 삼각형만)
            plt.annotate('', xy=(left_x - 1, base_y), xytext=(left_x - 1, apex_y), arrowprops=dict(arrowstyle='<->'))
            plt.text(left_x - 1.5, base_y + height / 2, f'{height:.1f} m', ha='center', va='center', rotation='vertical')
            
            # 내각 치수선 (호 그리기)
            arc_radius = 3
            arc = patches.Arc((left_x, left_y), arc_radius, arc_radius, angle=0, theta1=0, theta2=np.degrees(a), color='black')
            plt.gca().add_patch(arc)

            # 각도 표시 (호 끝부분 근처에 배치)
            angle_deg = np.degrees(a)
            arc_end_x = left_x + arc_radius * np.cos(np.radians(angle_deg / 2))
            arc_end_y = left_y + arc_radius * np.sin(np.radians(angle_deg / 2))
            plt.text(arc_end_x + 0.5, arc_end_y, f'{angle_deg:.2f}°', ha='center', va='center')

        # 시작점과 끝점 표시 (투명도 조절)
        if i == 0:
            plt.plot(left_x, left_y, 'r^', markersize=10, alpha=0.7, markerfacecolor='r', markeredgewidth=0)
        elif i == n - 1:
            plt.plot(right_x, right_y, 'ro', markersize=10, alpha=0.7, markerfacecolor='r', markeredgewidth=0)

    # 전체 길이 치수선
    total_length = n * base_length
    plt.annotate('', xy=(0, -2), xytext=(total_length, -2), arrowprops=dict(arrowstyle='<->'))
    plt.text(total_length / 2, -2.5, f'{total_length:.1f} m', ha='center', va='center')

    # 위 꼭지점들을 직선으로 연결
    apex_x_points, apex_y_points = zip(*apex_points)
    plt.plot(apex_x_points, apex_y_points, 'b-')

    # 꼭지점 직선 길이 치수선
    plt.annotate('', xy=(apex_x_points[0], apex_y_points[0] + 1), xytext=(apex_x_points[-1], apex_y_points[-1] + 1), arrowprops=dict(arrowstyle='<->'))
    apex_line_length = np.sqrt((apex_x_points[-1] - apex_x_points[0]) ** 2 + (apex_y_points[-1] - apex_y_points[0]) ** 2)
    plt.text((apex_x_points[0] + apex_x_points[-1]) / 2, apex_y_points[0] + 1.5, f'{apex_line_length:.1f} m', ha='center', va='center')

    # 그래프 제목 설정
    plt.title('주교')

    # 축 범위 설정
    plt.xlim(-5, total_length + 5)
    plt.ylim(-5, height + 5)

    # 축 절편값 제거
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])

    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)

    # 부재력과 응력 표를 아래에 가운데 정렬하여 표시
    column_labels = ["Member", "Force (kN)", "Stress (N/mm^2)"]
    cell_text = [[f"F{i}", f"{force:.2f}", f"{stress:.2f}"] for i, (force, stress) in enumerate(zip(forces, stresses), 1)]
    
    plt.subplots_adjust(bottom=0.4)
    ax = plt.gca()
    table = plt.table(cellText=cell_text, colLabels=column_labels, cellLoc='center', loc='bottom', colWidths=[0.2, 0.2, 0.2], bbox=[0.1, -2.5, 0.8, 2.3])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(2, 2)

    plt.show()

# 예제 데이터
# forces = [10, 15, 20, 25, 30, 35]
# stresses = [100, 150, 200, 250, 300, 350]
# draw_bridge_and_forces(forces, stresses, height=5)

