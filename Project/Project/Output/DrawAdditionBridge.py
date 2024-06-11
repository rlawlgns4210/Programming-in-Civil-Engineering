import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 또는 'AppleGothic' for macOS
plt.rcParams['axes.unicode_minus'] = False

def draw_addition_bridge_and_forces(forces, stresses, height, num_panels, save_path=None):
    a = np.arctan(2)

    base_length = 10
    height = base_length / 2 * np.tan(a)
    apex_points = []

    plt.figure(figsize=(14, 14))

    for i in range(num_panels):
        base_x = i * base_length
        base_y = 0
        left_x = base_x
        left_y = base_y
        right_x = base_x + base_length
        right_y = base_y
        apex_x = base_x + base_length / 2
        apex_y = base_y + height
        apex_points.append((apex_x, apex_y))

        triangle_x = [left_x, apex_x, right_x, left_x]
        triangle_y = [left_y, apex_y, right_y, left_y]
        plt.plot(triangle_x, triangle_y, 'b-')

        if i == 0:
            plt.annotate('', xy=(left_x - 1, base_y), xytext=(left_x - 1, apex_y), arrowprops=dict(arrowstyle='<->'))
            plt.text(left_x - 1.5, base_y + height / 2, f'{height:.1f} m', ha='center', va='center', rotation='vertical')
            arc_radius = 3
            arc = patches.Arc((left_x, left_y), arc_radius, arc_radius, angle=0, theta1=0, theta2=np.degrees(a), color='black')
            plt.gca().add_patch(arc)
            angle_deg = np.degrees(a)
            arc_end_x = left_x + arc_radius * np.cos(np.radians(angle_deg / 2))
            arc_end_y = left_y + arc_radius * np.sin(np.radians(angle_deg / 2))
            plt.text(arc_end_x + 0.5, arc_end_y, f'{angle_deg:.2f}°', ha='center', va='center')

        if i == 0:
            plt.plot(left_x, left_y, 'r^', markersize=10, alpha=0.7, markerfacecolor='r', markeredgewidth=0)
        elif i == num_panels - 1:
            plt.plot(right_x, right_y, 'ro', markersize=10, alpha=0.7, markerfacecolor='r', markeredgewidth=0)

    total_length = num_panels * base_length
    plt.annotate('', xy=(0, -2), xytext=(total_length, -2), arrowprops=dict(arrowstyle='<->'))
    plt.text(total_length / 2, -2.5, f'{total_length:.1f} m', ha='center', va='center')

    apex_x_points, apex_y_points = zip(*apex_points)
    plt.plot(apex_x_points, apex_y_points, 'b-')

    plt.annotate('', xy=(apex_x_points[0], apex_y_points[0] + 1), xytext=(apex_x_points[-1], apex_y_points[-1] + 1), arrowprops=dict(arrowstyle='<->'))
    apex_line_length = np.sqrt((apex_x_points[-1] - apex_x_points[0]) ** 2 + (apex_y_points[-1] - apex_y_points[0]) ** 2)
    plt.text((apex_x_points[0] + apex_x_points[-1]) / 2, apex_y_points[0] + 1.5, f'{apex_line_length:.1f} m', ha='center', va='center')

    plt.title('추가 교량')
    plt.xlim(-5, total_length + 5)
    plt.ylim(-5, height + 5)
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)

    column_labels = ["Member", "Force (kN)", "Stress (N/mm^2)"]
    cell_text = []

    for i in range(1, 4 * num_panels):
        cell_text.append([f"F{i}", f"{forces[i-1]:.2f}", f"{stresses[i-1]:.2f}"])

    plt.subplots_adjust(bottom=0.4)
    ax = plt.gca()
    table = plt.table(cellText=cell_text, colLabels=column_labels, cellLoc='center', loc='bottom', colWidths=[0.2, 0.2, 0.2], bbox=[0.1, -2.5, 0.8, 2.3])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(2, 2)

    if save_path:
        plt.savefig(save_path)
    
    plt.show()
