import math

class BridgeInform:
    def __init__(self, linear_density, load_distribution, bridge_length):
        self.linear_density = linear_density  # 교량의 선형 밀도 (kg/m)
        self.load_distribution = load_distribution  # 분포 하중 (kN/m)
        self.bridge_length = bridge_length  # 교량의 총 길이 (m)
        
    def calculate_panel_values(self):
        total_bridge_length = self.bridge_length  # 총 교량 길이
        
        if total_bridge_length > 60:
            bridge_length = 60
            num_panels = 6
            num_bridges = total_bridge_length // 60  # 60m 길이의 교량 개수
            remaining_bridge_length = total_bridge_length - (num_bridges * 60)  # 남은 교량 길이
        else:
            bridge_length = total_bridge_length
            num_panels = max(1, int(total_bridge_length / 10))  # 패널 개수 (최소 1개)
            num_bridges = 1
            remaining_bridge_length = total_bridge_length - (num_panels * 10)  # 남은 교량 길이
        
        # 자중 계산 (N/m 단위로 변환 후 kN/m로 변환)
        self_weight = (4.236 * num_panels - 1) * self.linear_density * 9.81 / num_panels / 1000  
        
        distributed_load = self.load_distribution  # 분포 하중
        total_load = self_weight + distributed_load  # 총 하중
        node_load = 10 * total_load  # 노드 하중
        num_nodes = 2 * num_panels + 1  # 노드 개수
        support_reaction = 5 * total_load * num_panels  # 지지 반력
        support_load = 5 * total_load  # 지지 하중
        support_resultant_force = support_reaction - support_load  # 지지 결과 힘
        angle = math.degrees(math.atan(2))  # 각도 계산
        
        # 계산 결과 반환
        return (
            total_bridge_length, num_bridges, bridge_length, remaining_bridge_length, 
            self_weight, distributed_load, total_load, node_load, num_nodes, 
            support_reaction, support_resultant_force, angle
        )


class SideBridge6(BridgeInform):
    def __init__(self, linear_density, load_distribution, remaining_bridge_length, cross_section_area):
        super().__init__(linear_density, load_distribution, remaining_bridge_length)
        self.remaining_bridge_length = remaining_bridge_length
        self.cross_section_area = cross_section_area
        self.num_panels = 6
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        l = self.remaining_bridge_length 
        b = math.degrees(math.atan(10 / (l + 5)))
        a = math.degrees(math.atan(2))
        
        w1 = (4.236 * self.num_panels - 1) * self.linear_density * 9.81 / (self.num_panels * 1000) + (self.linear_density * 9.81 * ((l * (math.cos(math.radians(b)) + 1) + 5) / math.cos(math.radians(b)))) / l
        # w1을 N/m에서 kN/m로 변환
        w1 /= 1000  
        
        w2 = self.load_distribution
        W = w1 + w2
        
        Ra = W * (5 * self.num_panels + l + l**2 / (20 * self.num_panels))
        Rb = W * (5 * self.num_panels - l**2 / (20 * self.num_panels))
        Pa = Ra - W * l / 2 - 5 * W
        Pb = Rb - W * l / 2 - 5 * W
        # 부재력 계산
        Fs1 = W * l / (2 * math.sin(math.radians(b)))
        Fs2 = -Fs1 * math.cos(math.radians(b))
        F1 = -Pa / math.sin(math.radians(a))
        F2 = Fs2 - F1 * math.cos(math.radians(a))
        F3 = (Fs1 * math.sin(math.radians(b)) + F1 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F4 = Fs1 * math.cos(math.radians(b)) + F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F7 = -F5
        F8 = F4 + F5 * math.cos(math.radians(a)) - F7 * math.cos(math.radians(a))
        F9 = (10 * W - F7 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F10 = F6 + F7 * math.cos(math.radians(a)) - F9 * math.cos(math.radians(a))
        F11 = -F9
        F12 = F8 + F9 * math.cos(math.radians(a)) - F11 * math.cos(math.radians(a))
        F23 = -Pb / math.sin(math.radians(a))
        F22 = -F23 * math.cos(math.radians(a))
        F21 = -F23
        F20 = F21 * math.cos(math.radians(a)) - F23 * math.cos(math.radians(a))
        F19 = (10 * W - F21 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F18 = -F19 * math.cos(math.radians(a)) + F21 * math.cos(math.radians(a)) + F22
        F17 = -F19
        F16 = -F17 * math.cos(math.radians(a)) + F19 * math.cos(math.radians(a)) + F20
        F15 = (10 * W - F17 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F14 = -F15 * math.cos(math.radians(a)) + F17 * math.cos(math.radians(a)) + F18
        F13 = -F15
        # F13 = (10 * W - F11 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F14 = F10 + F11 * math.cos(math.radians(a)) - F13 * math.cos(math.radians(a))
        # F15 = -F13
        # F16 = F12 + F13 * math.cos(math.radians(a)) - F15 * math.cos(math.radians(a))
        # F17 = (10 * W - F15 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F18 = F14 + F15 * math.cos(math.radians(a)) - F17 * math.cos(math.radians(a))
        # F19 = -F17
        # F20 = F16 + F17 * math.cos(math.radians(a)) - F19 * math.cos(math.radians(a))
        # F21 = (10 * W - F19 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F22 = F18 + F19 * math.cos(math.radians(a)) - F21 * math.cos(math.radians(a))
        # F23 = -F21

        self.member_forces = [Fs1, Fs2, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'l': l, 'b': b, 'a': a, 'w1': w1, 'w2': w2, 'W': W,
            'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"l = {details['l']:.2f} m")
        print(f"b = {details['b']:.2f} degrees")
        print(f"a = {details['a']:.2f} degrees")
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        
        if force_limit:
            forces = forces[:force_limit + 2]  # Including Fs1 and Fs2
            stress_forces = stress_forces[:force_limit + 2]
        
        print(f"Fs1 = {forces[0]:.2f} kN, stress_Fs1 = {stress_forces[0]:.2f} N/mm^2")
        print(f"Fs2 = {forces[1]:.2f} kN, stress_Fs2 = {stress_forces[1]:.2f} N/mm^2")

        for i, (force, stress) in enumerate(zip(forces[2:], stress_forces[2:]), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")


class SideBridge5(BridgeInform):
    def __init__(self, linear_density, load_distribution, remaining_bridge_length, cross_section_area):
        super().__init__(linear_density, load_distribution, remaining_bridge_length)
        self.remaining_bridge_length = remaining_bridge_length
        self.cross_section_area = cross_section_area
        self.num_panels = 5
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        l = self.remaining_bridge_length 
        b = math.degrees(math.atan(10 / (l + 5)))
        a = math.degrees(math.atan(2))
        
        w1 = (4.236 * self.num_panels - 1) * self.linear_density * 9.81 / (self.num_panels * 1000) + (self.linear_density * 9.81 * ((l * (math.cos(math.radians(b)) + 1) + 5) / math.cos(math.radians(b)))) / l
        # w1을 N/m에서 kN/m로 변환
        w1 /= 1000  
        
        w2 = self.load_distribution
        W = w1 + w2
        
        Ra = W * (5 * self.num_panels + l + l**2 / (20 * self.num_panels))
        Rb = W * (5 * self.num_panels - l**2 / (20 * self.num_panels))
        Pa = Ra - W * l / 2 - 5 * W
        Pb = Rb - W * l / 2 - 5 * W
        # 부재력 계산
        Fs1 = W * l / (2 * math.sin(math.radians(b)))
        Fs2 = -Fs1 * math.cos(math.radians(b))
        F1 = -Pa / math.sin(math.radians(a))
        F2 = Fs2 - F1 * math.cos(math.radians(a))
        F3 = (Fs1 * math.sin(math.radians(b)) + F1 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F4 = Fs1 * math.cos(math.radians(b)) + F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F7 = -F5
        F8 = F4 + F5 * math.cos(math.radians(a)) - F7 * math.cos(math.radians(a))
        F9 = (10 * W - F7 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F10 = F6 + F7 * math.cos(math.radians(a)) - F9 * math.cos(math.radians(a))
        F11 = -F9
        F12 = F8 + F9 * math.cos(math.radians(a)) - F11 * math.cos(math.radians(a))
        F19 = -Pb / math.sin(math.radians(a))
        F18 = -F19 * math.cos(math.radians(a))
        F17 = -F19
        F16 = -F17 * math.cos(math.radians(a)) + F19 * math.cos(math.radians(a))
        F15 = (10 * W - F17 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F14 = -F15 * math.cos(math.radians(a)) + F17 * math.cos(math.radians(a)) + F18
        F13 = -F15
        # F13 = (10 * W - F11 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F14 = F10 + F11 * math.cos(math.radians(a)) - F13 * math.cos(math.radians(a))
        # F15 = -F13
        # F16 = F12 + F13 * math.cos(math.radians(a)) - F15 * math.cos(math.radians(a))
        # F17 = (10 * W - F15 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F18 = F14 + F15 * math.cos(math.radians(a)) - F17 * math.cos(math.radians(a))
        # F19 = -F17

        self.member_forces = [Fs1, Fs2, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'l': l, 'b': b, 'a': a, 'w1': w1, 'w2': w2, 'W': W,
            'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"l = {details['l']:.2f} m")
        print(f"b = {details['b']:.2f} degrees")
        print(f"a = {details['a']:.2f} degrees")
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        
        if force_limit:
            forces = forces[:force_limit + 2]  # Including Fs1 and Fs2
            stress_forces = stress_forces[:force_limit + 2]
        
        print(f"Fs1 = {forces[0]:.2f} kN, stress_Fs1 = {stress_forces[0]:.2f} N/mm^2")
        print(f"Fs2 = {forces[1]:.2f} kN, stress_Fs2 = {stress_forces[1]:.2f} N/mm^2")

        for i, (force, stress) in enumerate(zip(forces[2:], stress_forces[2:]), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")


class SideBridge4(BridgeInform):
    def __init__(self, linear_density, load_distribution, remaining_bridge_length, cross_section_area):
        super().__init__(linear_density, load_distribution, remaining_bridge_length)
        self.remaining_bridge_length = remaining_bridge_length
        self.cross_section_area = cross_section_area
        self.num_panels = 4
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        l = self.remaining_bridge_length 
        b = math.degrees(math.atan(10 / (l + 5)))
        a = math.degrees(math.atan(2))
        
        w1 = (4.236 * self.num_panels - 1) * self.linear_density * 9.81 / (self.num_panels * 1000) + (self.linear_density * 9.81 * ((l * (math.cos(math.radians(b)) + 1) + 5) / math.cos(math.radians(b)))) / l
        # w1을 N/m에서 kN/m로 변환
        w1 /= 1000  
        
        w2 = self.load_distribution
        W = w1 + w2
        
        Ra = W * (5 * self.num_panels + l + l**2 / (20 * self.num_panels))
        Rb = W * (5 * self.num_panels - l**2 / (20 * self.num_panels))
        Pa = Ra - W * l / 2 - 5 * W
        Pb = Rb - W * l / 2 - 5 * W
        # 부재력 계산
        Fs1 = W * l / (2 * math.sin(math.radians(b)))
        Fs2 = -Fs1 * math.cos(math.radians(b))
        F1 = -Pa / math.sin(math.radians(a))
        F2 = Fs2 - F1 * math.cos(math.radians(a))
        F3 = (Fs1 * math.sin(math.radians(b)) + F1 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F4 = Fs1 * math.cos(math.radians(b)) + F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F7 = -F5
        F8 = F4 + F5 * math.cos(math.radians(a)) - F7 * math.cos(math.radians(a))
        F15 = -Pb / math.sin(math.radians(a))
        F14 = -F15 * math.cos(math.radians(a))
        F13 = -F15
        F12 = -F13 * math.cos(math.radians(a)) + F15 * math.cos(math.radians(a))
        F11 = (10 * W - F13 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F10 = -F11 * math.cos(math.radians(a)) + F13 * math.cos(math.radians(a)) + F14
        F9 = -F11
        # F9 = (10 * W - F7 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F10 = F6 + F7 * math.cos(math.radians(a)) - F9 * math.cos(math.radians(a))
        # F11 = -F9
        # F12 = F8 + F9 * math.cos(math.radians(a)) - F11 * math.cos(math.radians(a))
        # F13 = (10 * W - F11 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F14 = F10 + F11 * math.cos(math.radians(a)) - F13 * math.cos(math.radians(a))
        # F15 = -F13

        self.member_forces = [Fs1, Fs2, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'l': l, 'b': b, 'a': a, 'w1': w1, 'w2': w2, 'W': W,
            'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"l = {details['l']:.2f} m")
        print(f"b = {details['b']:.2f} degrees")
        print(f"a = {details['a']:.2f} degrees")
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        
        if force_limit:
            forces = forces[:force_limit + 2]  # Including Fs1 and Fs2
            stress_forces = stress_forces[:force_limit + 2]
        
        print(f"Fs1 = {forces[0]:.2f} kN, stress_Fs1 = {stress_forces[0]:.2f} N/mm^2")
        print(f"Fs2 = {forces[1]:.2f} kN, stress_Fs2 = {stress_forces[1]:.2f} N/mm^2")

        for i, (force, stress) in enumerate(zip(forces[2:], stress_forces[2:]), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")


class SideBridge3(BridgeInform):
    def __init__(self, linear_density, load_distribution, remaining_bridge_length, cross_section_area):
        super().__init__(linear_density, load_distribution, remaining_bridge_length)
        self.remaining_bridge_length = remaining_bridge_length
        self.cross_section_area = cross_section_area
        self.num_panels = 3
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        l = self.remaining_bridge_length 
        b = math.degrees(math.atan(10 / (l + 5)))
        a = math.degrees(math.atan(2))
        
        w1 = (4.236 * self.num_panels - 1) * self.linear_density * 9.81 / (self.num_panels * 1000) + (self.linear_density * 9.81 * ((l * (math.cos(math.radians(b)) + 1) + 5) / math.cos(math.radians(b)))) / l
        # w1을 N/m에서 kN/m로 변환
        w1 /= 1000  
        
        w2 = self.load_distribution
        W = w1 + w2
        
        Ra = W * (5 * self.num_panels + l + l**2 / (20 * self.num_panels))
        Rb = W * (5 * self.num_panels - l**2 / (20 * self.num_panels))
        Pa = Ra - W * l / 2 - 5 * W
        Pb = Rb - W * l / 2 - 5 * W
        # 부재력 계산
        Fs1 = W * l / (2 * math.sin(math.radians(b)))
        Fs2 = -Fs1 * math.cos(math.radians(b))
        F1 = -Pa / math.sin(math.radians(a))
        F2 = Fs2 - F1 * math.cos(math.radians(a))
        F3 = (Fs1 * math.sin(math.radians(b)) + F1 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F4 = Fs1 * math.cos(math.radians(b)) + F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F11 = -Pb / math.sin(math.radians(a))
        F10 = -F11 * math.cos(math.radians(a))
        F9 = -F11
        F8 = -F9 * math.cos(math.radians(a)) + F11 * math.cos(math.radians(a))
        F7 = (10 * W - F9 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        
        # F7 = -F5
        # F8 = F4 + F5 * math.cos(math.radians(a)) - F7 * math.cos(math.radians(a))
        # F9 = (10 * W - F7 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F10 = F6 + F7 * math.cos(math.radians(a)) - F9 * math.cos(math.radians(a))
        # F11 = -F9
        

        self.member_forces = [Fs1, Fs2, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'l': l, 'b': b, 'a': a, 'w1': w1, 'w2': w2, 'W': W,
            'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"l = {details['l']:.2f} m")
        print(f"b = {details['b']:.2f} degrees")
        print(f"a = {details['a']:.2f} degrees")
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        
        if force_limit:
            forces = forces[:force_limit + 2]  # Including Fs1 and Fs2
            stress_forces = stress_forces[:force_limit + 2]
        
        print(f"Fs1 = {forces[0]:.2f} kN, stress_Fs1 = {stress_forces[0]:.2f} N/mm^2")
        print(f"Fs2 = {forces[1]:.2f} kN, stress_Fs2 = {stress_forces[1]:.2f} N/mm^2")

        for i, (force, stress) in enumerate(zip(forces[2:], stress_forces[2:]), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")


class SideBridge2(BridgeInform):
    def __init__(self, linear_density, load_distribution, remaining_bridge_length, cross_section_area):
        super().__init__(linear_density, load_distribution, remaining_bridge_length)
        self.remaining_bridge_length = remaining_bridge_length
        self.cross_section_area = cross_section_area
        self.num_panels = 2
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        l = self.remaining_bridge_length 
        b = math.degrees(math.atan(10 / (l + 5)))
        a = math.degrees(math.atan(2))
        
        w1 = (4.236 * self.num_panels - 1) * self.linear_density * 9.81 / (self.num_panels * 1000) + (self.linear_density * 9.81 * ((l * (math.cos(math.radians(b)) + 1) + 5) / math.cos(math.radians(b)))) / l
        # w1을 N/m에서 kN/m로 변환
        w1 /= 1000  
        
        w2 = self.load_distribution
        W = w1 + w2
        
        Ra = W * (5 * self.num_panels + l + l**2 / (20 * self.num_panels))
        Rb = W * (5 * self.num_panels - l**2 / (20 * self.num_panels))
        Pa = Ra - W * l / 2 - 5 * W
        Pb = Rb - W * l / 2 - 5 * W
        # 부재력 계산
        Fs1 = W * l / (2 * math.sin(math.radians(b)))
        Fs2 = -Fs1 * math.cos(math.radians(b))
        F1 = -Pa / math.sin(math.radians(a))
        F2 = Fs2 - F1 * math.cos(math.radians(a))
        F3 = (Fs1 * math.sin(math.radians(b)) + F1 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F4 = Fs1 * math.cos(math.radians(b)) + F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F7 = -Pb/math.sin(math.radians(a))
        F6 = -F7 * math.cos(math.radians(a))
        F5 = -F7
        # F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        # F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        # F7 = -F5
        

        self.member_forces = [Fs1, Fs2, F1, F2, F3, F4, F5, F6, F7]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'l': l, 'b': b, 'a': a, 'w1': w1, 'w2': w2, 'W': W,
            'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"l = {details['l']:.2f} m")
        print(f"b = {details['b']:.2f} degrees")
        print(f"a = {details['a']:.2f} degrees")
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        
        if force_limit:
            forces = forces[:force_limit + 2]  # Including Fs1 and Fs2
            stress_forces = stress_forces[:force_limit + 2]
        
        print(f"Fs1 = {forces[0]:.2f} kN, stress_Fs1 = {stress_forces[0]:.2f} N/mm^2")
        print(f"Fs2 = {forces[1]:.2f} kN, stress_Fs2 = {stress_forces[1]:.2f} N/mm^2")

        for i, (force, stress) in enumerate(zip(forces[2:], stress_forces[2:]), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")



class MainBridge(BridgeInform):
    def __init__(self, linear_density, load_distribution, bridge_length, cross_section_area, num_panels):
        super().__init__(linear_density, load_distribution, bridge_length)
        self.num_panels = num_panels
        self.cross_section_area = cross_section_area
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        w1 = ((4.236 * self.num_panels - 1) * self.linear_density * 9.81) / (1000 * self.num_panels)
        w2 = self.load_distribution
        W = w1 + w2
        a = math.degrees(math.atan(2))
        
        Ra = self.num_panels * 5 * W
        Rb = self.num_panels * 5 * W
        Pa = Ra - 5 * W
        Pb = Rb - 5 * W
        
        F1 = -Pa / math.sin(math.radians(a))
        F2 = -F1 * math.cos(math.radians(a))
        F3 = -F1
        F4 = F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F7 = -F5
        F8 = F4 + F5 * math.cos(math.radians(a)) - F7 * math.cos(math.radians(a))
        F9 = (10 * W - F7 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F10 = F6 + F7 * math.cos(math.radians(a)) - F9 * math.cos(math.radians(a))
        F11 = -F9
        F12 = F8 + F9 * math.cos(math.radians(a)) - F11 * math.cos(math.radians(a))
        F13 = (10 * W - F11 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F14 = F10 + F11 * math.cos(math.radians(a)) - F13 * math.cos(math.radians(a))
        F15 = -F13
        F16 = F12 + F13 * math.cos(math.radians(a)) - F15 * math.cos(math.radians(a))
        F17 = (10 * W - F15 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F18 = F14 + F15 * math.cos(math.radians(a)) - F17 * math.cos(math.radians(a))
        F19 = -F17
        F20 = F16 + F17 * math.cos(math.radians(a)) - F19 * math.cos(math.radians(a))
        F21 = (10 * W - F19 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F22 = F18 + F19 * math.cos(math.radians(a)) - F21 * math.cos(math.radians(a))
        F23 = -F21 

        self.member_forces = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'w1': w1, 'w2': w2, 'W': W, 'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb, 'a': a
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        print(f"a = {details['a']:.2f} degrees")
        
        if force_limit:
            forces = forces[:force_limit]
            stress_forces = stress_forces[:force_limit]
        
        for i, (force, stress) in enumerate(zip(forces, stress_forces), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")




class AdditionBridge5(BridgeInform):
    def __init__(self, linear_density, load_distribution, cross_section_area, num_panels):
        super().__init__(linear_density, load_distribution, num_panels)
        self.num_panels = 5
        self.cross_section_area = cross_section_area
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        w1 = ((4.236 * self.num_panels - 1) * self.linear_density * 9.81) / (1000 * self.num_panels)
        w2 = self.load_distribution
        W = w1 + w2
        a = math.degrees(math.atan(2))
        
        Ra = self.num_panels * 5 * W
        Rb = self.num_panels * 5 * W
        Pa = Ra - 5 * W
        Pb = Rb - 5 * W
        
        F1 = -Pa / math.sin(math.radians(a))
        F2 = -F1 * math.cos(math.radians(a))
        F3 = -F1
        F4 = F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F7 = -F5
        F8 = F4 + F5 * math.cos(math.radians(a)) - F7 * math.cos(math.radians(a))
        F9 = (10 * W - F7 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F10 = F6 + F7 * math.cos(math.radians(a)) - F9 * math.cos(math.radians(a))
        F11 = -F9
        F12 = F8 + F9 * math.cos(math.radians(a)) - F11 * math.cos(math.radians(a))
        F19 = -Pb / math.sin(math.radians(a))
        F18 = -F19 * math.cos(math.radians(a))
        F17 = -F19
        F16 = -F17 * math.cos(math.radians(a)) + F19 * math.cos(math.radians(a))
        F15 = (10 * W - F17 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F14 = -F15 * math.cos(math.radians(a)) + F17 * math.cos(math.radians(a)) + F18
        F13 = -F15

        self.member_forces = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19]
        
         # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'w1': w1, 'w2': w2, 'W': W, 'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb, 'a': a
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()

        if isinstance(forces, str):
            print(forces)
            return

        details = self.calculation_details
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        print(f"a = {details['a']:.2f} degrees")

        if force_limit:
            forces = forces[:force_limit]
            stress_forces = stress_forces[:force_limit]

        for i, (force, stress) in enumerate(zip(forces, stress_forces), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")



class AdditionBridge4(BridgeInform):
    def __init__(self, linear_density, load_distribution, cross_section_area, num_panels):
        super().__init__(linear_density, load_distribution, num_panels)
        self.num_panels = 4
        self.cross_section_area = cross_section_area
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        w1 = ((4.236 * self.num_panels - 1) * self.linear_density * 9.81) / (1000 * self.num_panels)
        w2 = self.load_distribution
        W = w1 + w2
        a = math.degrees(math.atan(2))
        
        Ra = self.num_panels * 5 * W
        Rb = self.num_panels * 5 * W
        Pa = Ra - 5 * W
        Pb = Rb - 5 * W
        
        F1 = -Pa / math.sin(math.radians(a))
        F2 = -F1 * math.cos(math.radians(a))
        F3 = -F1
        F4 = F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F7 = -F5
        F8 = F4 + F5 * math.cos(math.radians(a)) - F7 * math.cos(math.radians(a))
        F15 = -Pb / math.sin(math.radians(a))
        F14 = -F15 * math.cos(math.radians(a))
        F13 = -F15
        F12 = -F13 * math.cos(math.radians(a)) + F15 * math.cos(math.radians(a))
        F11 = (10 * W - F13 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F10 = -F11 * math.cos(math.radians(a)) + F13 * math.cos(math.radians(a)) + F14
        F9 = -F11
        
        self.member_forces = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'w1': w1, 'w2': w2, 'W': W, 'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb, 'a': a
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        print(f"a = {details['a']:.2f} degrees")
        
        if force_limit:
            forces = forces[:force_limit]
            stress_forces = stress_forces[:force_limit]
        
        for i, (force, stress) in enumerate(zip(forces, stress_forces), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")


class AdditionBridge3(BridgeInform):
    def __init__(self, linear_density, load_distribution, cross_section_area, num_panels):
        super().__init__(linear_density, load_distribution, num_panels)
        self.num_panels = 3
        self.cross_section_area = cross_section_area
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        w1 = ((4.236 * self.num_panels - 1) * self.linear_density * 9.81) / (1000 * self.num_panels)
        w2 = self.load_distribution
        W = w1 + w2
        a = math.degrees(math.atan(2))
        
        Ra = self.num_panels * 5 * W
        Rb = self.num_panels * 5 * W
        Pa = Ra - 5 * W
        Pb = Rb - 5 * W
        
        F1 = -Pa / math.sin(math.radians(a))
        F2 = -F1 * math.cos(math.radians(a))
        F3 = -F1
        F4 = F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F5 = (10 * W - F3 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        F6 = F2 + F3 * math.cos(math.radians(a)) - F5 * math.cos(math.radians(a))
        F11 = -Pb / math.sin(math.radians(a))
        F10 = -F11 * math.cos(math.radians(a))
        F9 = -F11
        F8 = -F9 * math.cos(math.radians(a)) + F11 * math.cos(math.radians(a))
        F7 = (10 * W - F9 * math.sin(math.radians(a))) / math.sin(math.radians(a))
        
        self.member_forces = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11]
        
         # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'w1': w1, 'w2': w2, 'W': W, 'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb, 'a': a
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()

        if isinstance(forces, str):
            print(forces)
            return

        details = self.calculation_details
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        print(f"a = {details['a']:.2f} degrees")

        if force_limit:
            forces = forces[:force_limit]
            stress_forces = stress_forces[:force_limit]

        for i, (force, stress) in enumerate(zip(forces, stress_forces), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")



class AdditionBridge2(BridgeInform):
    def __init__(self, linear_density, load_distribution, cross_section_area, num_panels):
        super().__init__(linear_density, load_distribution, num_panels)
        self.num_panels = 2
        self.cross_section_area = cross_section_area
        self.member_forces = []
        self.stress_forces = []
        self.calculation_details = {}

    def calculate_member_forces(self):
        w1 = ((4.236 * self.num_panels - 1) * self.linear_density * 9.81) / (1000 * self.num_panels)
        w2 = self.load_distribution
        W = w1 + w2
        a = math.degrees(math.atan(2))
        
        Ra = self.num_panels * 5 * W
        Rb = self.num_panels * 5 * W
        Pa = Ra - 5 * W
        Pb = Rb - 5 * W
        
        F1 = -Pa / math.sin(math.radians(a))
        F2 = -F1 * math.cos(math.radians(a))
        F3 = -F1
        F4 = F1 * math.cos(math.radians(a)) - F3 * math.cos(math.radians(a))
        F7 = -Pb/math.sin(math.radians(a))
        F6 = -F7 * math.cos(math.radians(a))
        F5 = -F7

        self.member_forces = [F1, F2, F3, F4, F5, F6, F7]
        
        # 부재력을 단면적으로 나눈 후, N/mm^2로 변환
        self.stress_forces = [1000 * force / self.cross_section_area for force in self.member_forces]
        # 필요한 추가 정보를 저장
        self.calculation_details = {
            'w1': w1, 'w2': w2, 'W': W, 'Ra': Ra, 'Rb': Rb, 'Pa': Pa, 'Pb': Pb, 'a': a
        }

        return self.member_forces, self.stress_forces

    def print_member_forces(self, force_limit=None):
        forces, stress_forces = self.calculate_member_forces()
        
        if isinstance(forces, str):
            print(forces)
            return
        
        details = self.calculation_details
        print(f"w1 = {details['w1']:.2f} kN/m")
        print(f"w2 = {details['w2']:.2f} kN/m")
        print(f"W = {details['W']:.2f} kN/m")
        print(f"Ra = {details['Ra']:.2f} kN")
        print(f"Rb = {details['Rb']:.2f} kN")
        print(f"Pa = {details['Pa']:.2f} kN")
        print(f"Pb = {details['Pb']:.2f} kN")
        print(f"a = {details['a']:.2f} degrees")
        
        if force_limit:
            forces = forces[:force_limit]
            stress_forces = stress_forces[:force_limit]
        
        for i, (force, stress) in enumerate(zip(forces, stress_forces), 1):
            force_type = "압축" if force < 0 else "인장"
            print(f"F{i} = {force:.2f} kN ({force_type}), stress_F{i} = {stress:.2f} N/mm^2")
