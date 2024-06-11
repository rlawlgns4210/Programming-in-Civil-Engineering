import os
import sys
import numpy as np
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# 현재 파일의 디렉토리 경로를 기준으로 상위 폴더 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)

# Output 폴더의 경로를 sys.path에 추가
output_dir = os.path.join(project_dir, 'Output')
sys.path.append(output_dir)

from LoadExcel import LoadExcel
from HBeamStandard import HBeamStandard
from IBeamStandard import IBeamStandard
from BridgeDesign import BridgeInform, SideBridge6, SideBridge5, SideBridge4, SideBridge3, SideBridge2, MainBridge, AdditionBridge5, AdditionBridge4, AdditionBridge3, AdditionBridge2
from DrawMainBridge import draw_bridge_and_forces # type: ignore
from DrawSideBridge import draw_side_bridge_and_forces # type: ignore
from DrawAdditionBridge import draw_addition_bridge_and_forces # type: ignore
from OutputInform import save_output_info # type: ignore

# Database 폴더의 database.xlsx 파일 경로
database_path = os.path.join(project_dir, 'Database', 'database.xlsx')

# 시트 이름 지정
sheet_name = 'input'  # 입력 시트 이름

# LoadExcel 인스턴스 생성
loader = LoadExcel(database_path, sheet_name)

# HBeamStandard 인스턴스 생성
h_beam_standard = HBeamStandard(loader)

# IBeamStandard 인스턴스 생성
i_beam_standard = IBeamStandard(loader)

# 데이터 불러오기 및 처리
df = loader.load_data()
if df is not None and not df.empty:  # 데이터 프레임이 비어있는지 여부 확인
    bridge_length, load_distribution, i_beam_spec, h_beam_spec, steel_material = loader.process_data(df)
    
    # H-Beam 규격에 따른 단면적 및 단위 무게 계산 및 출력
    if h_beam_spec != "[None, None, None, None]":
        cross_section_area, linear_density, section_modulus = h_beam_standard.calculate_specs(h_beam_spec)
        print("H-Beam 규격:", h_beam_spec)
        print("단면적(mm^2):", cross_section_area)
        print("단위무게(kg/m):", linear_density)
        print("단면계수(cm^3):", section_modulus)
    else:
        print("H-Beam 미사용")

    # I-Beam 규격에 따른 단면적 및 단위 무게 계산 및 출력
    if i_beam_spec != "[None, None, None, None, None]":
        cross_section_area, linear_density, section_modulus = i_beam_standard.calculate_specs(i_beam_spec)
        print("I-Beam 규격:", i_beam_spec)
        print("단면적(mm^2):", cross_section_area)
        print("단위무게(kg/m):", linear_density)
        print("단면계수(cm^3):", section_modulus)
    else:
        print("I-Beam 미사용")

    # BridgeInform을 사용하여 기본 계산 수행
    bridge_inform = BridgeInform(linear_density, load_distribution, bridge_length)
    total_bridge_length, num_bridges, bridge_length, remaining_bridge_length, self_weight, distributed_load, total_load, node_load, num_nodes, support_reaction, support_resultant_force, angle = bridge_inform.calculate_panel_values()
    
    # 첫 번째 MainBridge 실행
    num_panels = 6
    side_bridge_executed = False
    addition_bridge_executed = False
    print("\n첫 번째 MainBridge 실행 결과:")
    main_bridge = MainBridge(linear_density, load_distribution, remaining_bridge_length, cross_section_area, num_panels)
    main_bridge.print_member_forces()
    # remaining_bridge_length에 따른 조건에 따라 MainBridge, SideBridge 또는 AdditionBridge 실행
    while remaining_bridge_length > 0:
        if remaining_bridge_length > 50:
            num_panels = 5
            remaining_bridge_length -= 50
            print("\nSideBridge5 실행 결과 (num_panels = 5):")
            side_bridge = SideBridge5(linear_density, load_distribution, remaining_bridge_length, cross_section_area)
            side_bridge.print_member_forces(force_limit=19)
            side_bridge_executed = True
            break
        elif remaining_bridge_length == 50:
            num_panels = 5
            print("\n추가 MainBridge 실행 결과 (num_panels = 5):")
            addition_bridge = AdditionBridge5(linear_density, load_distribution, cross_section_area, num_panels)
            addition_bridge.print_member_forces(force_limit=19)
            addition_bridge_executed = True
            break
        elif remaining_bridge_length > 40:
            num_panels = 4
            remaining_bridge_length -= 40
            print("\nSideBridge4 실행 결과 (num_panels = 4):")
            side_bridge = SideBridge4(linear_density, load_distribution, remaining_bridge_length, cross_section_area)
            side_bridge.print_member_forces(force_limit=15)
            side_bridge_executed = True
            break
        elif remaining_bridge_length == 40:
            num_panels = 4
            print("\n추가 MainBridge 실행 결과 (num_panels = 4):")
            addition_bridge = AdditionBridge4(linear_density, load_distribution, cross_section_area, num_panels)
            addition_bridge.print_member_forces(force_limit=15)
            addition_bridge_executed = True
            break
        elif remaining_bridge_length > 30:
            num_panels = 3
            remaining_bridge_length -= 30
            print("\nSideBridge3 실행 결과 (num_panels = 3):")
            side_bridge = SideBridge3(linear_density, load_distribution, remaining_bridge_length, cross_section_area)
            side_bridge.print_member_forces(force_limit=11)
            side_bridge_executed = True
            break
        elif remaining_bridge_length == 30:
            num_panels = 3
            print("\n추가 MainBridge 실행 결과 (num_panels = 3):")
            addition_bridge = AdditionBridge3(linear_density, load_distribution, cross_section_area, num_panels)
            addition_bridge.print_member_forces(force_limit=11)
            addition_bridge_executed = True
            break
        elif remaining_bridge_length > 20:
            num_panels = 2
            remaining_bridge_length -= 20
            print("\nSideBridge2 실행 결과 (num_panels = 2):")
            side_bridge = SideBridge2(linear_density, load_distribution, remaining_bridge_length, cross_section_area)
            side_bridge.print_member_forces(force_limit=7)
            side_bridge_executed = True
            break
        elif remaining_bridge_length == 20:
            num_panels = 2
            print("\n추가 MainBridge 실행 결과 (num_panels = 2):")
            addition_bridge = AdditionBridge2(linear_density, load_distribution, cross_section_area, num_panels)
            addition_bridge.print_member_forces(force_limit=7)
            addition_bridge_executed = True
            break
        elif remaining_bridge_length < 20:
            num_panels = 6
            print("\nSideBridge6 실행 결과 (num_panels = 6):")
            side_bridge = SideBridge6(linear_density, load_distribution, remaining_bridge_length, cross_section_area)
            side_bridge.print_member_forces()
            side_bridge_executed = True
            break
    # 계산 결과 출력 또는 활용
    print("\n전체 길이(m):", total_bridge_length)
    print("교량 길이(m):", bridge_length)
    
    if side_bridge_executed:
        if isinstance(side_bridge, SideBridge6):
            num_bridges -= 1
            print("주교 개수:", int(num_bridges))
            num_side_bridge = 1
            print("측교 개수:", num_side_bridge)
            num_addition_bridge = 0
        else:
            print("주교 개수:", int(num_bridges))
            num_side_bridge = 1
            print("측교 개수:", num_side_bridge)
            num_addition_bridge = 0
    elif addition_bridge_executed:
        num_side_bridge = 0
        print("주교 개수:", int(num_bridges))
        num_addition_bridge = 1
        print("추가 교량 개수:", num_addition_bridge)
    else:
        num_side_bridge = 0
        num_addition_bridge = 0
        print("주교 개수:", int(num_bridges))
        
    # print("남은 교량 길이(m):", remaining_bridge_length)
    print("자중(kN/m):", self_weight)
    print("분포 하중(kN/m):", distributed_load)
    print("총 하중(kN):", total_load)
    print("절점 하중(kN):", node_load)
    # print("절점 수:", num_nodes)
    print("지점 반력(kN):", support_reaction)
    print("지점 합력(kN):", support_resultant_force)
    print("각도(˚):", angle)

    # 높이 계산
    height = 10 / 2 * np.tan(np.arctan(2))

    # 그래프 저장 경로 설정
    main_bridge_image_path = os.path.join(output_dir, 'main_bridge.png')
    side_bridge_image_path = os.path.join(output_dir, 'side_bridge.png')
    addition_bridge_image_path = os.path.join(output_dir, 'addition_bridge.png')

    # 그래프 그리기 및 저장
    draw_bridge_and_forces(main_bridge.member_forces, main_bridge.stress_forces, height, save_path=main_bridge_image_path)
    
    if side_bridge_executed:
        draw_side_bridge_and_forces(side_bridge.member_forces, side_bridge.stress_forces, height, remaining_bridge_length, num_panels, save_path=side_bridge_image_path)
    
    if addition_bridge_executed:
        draw_addition_bridge_and_forces(addition_bridge.member_forces, addition_bridge.stress_forces, height, num_panels, save_path=addition_bridge_image_path)
    
    # OutputInform.xlsx 파일 저장
    save_output_info(main_bridge, side_bridge if side_bridge_executed else None, addition_bridge if addition_bridge_executed else None, num_bridges, num_side_bridge, num_addition_bridge, remaining_bridge_length, steel_material, num_panels)

    # 그래프 이미지 추가
    workbook = load_workbook('OutputInform.xlsx')
    if main_bridge_image_path:
        img = Image(main_bridge_image_path)
        img.anchor = 'F2'
        workbook['mainbridge'].add_image(img)
    if side_bridge_image_path and side_bridge_executed:
        img = Image(side_bridge_image_path)
        img.anchor = 'F2'
        workbook['sidebridge'].add_image(img)
    if addition_bridge_image_path and addition_bridge_executed:
        img = Image(addition_bridge_image_path)
        img.anchor = 'F2'
        workbook['additionbridge'].add_image(img)

    workbook.save('OutputInform.xlsx')
else:
    print("Failed to load data from Excel.")
