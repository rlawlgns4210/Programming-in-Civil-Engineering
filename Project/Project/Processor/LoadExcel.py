import os
import pandas as pd

class LoadExcel:
    def __init__(self, database_path, sheet_name):
        self.database_path = database_path
        self.sheet_name = sheet_name

    def load_data(self):
        try:
            df = pd.read_excel(self.database_path, sheet_name=self.sheet_name)
            return df
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {self.database_path}")
            return None
        except Exception as e:
            print(f"파일을 불러오는 중 오류가 발생했습니다: {e}")
            return None

    def process_data(self, df):
        last_row = df.iloc[-1]
        bridge_length = last_row['교량길이']
        bridge_length_unit = last_row['교량길이 단위']
        load_distribution = last_row['분포하중']
        load_distribution_unit = last_row['분포하중 단위']
        i_beam_spec = last_row['I-Beam 규격']
        h_beam_spec = last_row['H-Beam 규격']
        steel_material = last_row['강재']

        # 단위 변환
        if bridge_length_unit == 'mm':
            bridge_length *= 0.001  # mm를 m로 변환
        elif bridge_length_unit == 'cm':
            bridge_length *= 0.01  # cm를 m로 변환
        elif bridge_length_unit == 'km':
            bridge_length *= 1000  # km를 m로 변환

        if load_distribution_unit == 'N/m':
            load_distribution *= 0.001  # N/m를 kN/m로 변환

        # 마지막 요소 수정
        if isinstance(i_beam_spec, str) and i_beam_spec:
            i_beam_spec = i_beam_spec.rsplit(',', 1)[0].strip() + ']'

        if isinstance(h_beam_spec, str) and h_beam_spec:
            h_beam_spec = h_beam_spec.rsplit(',', 1)[0].strip() + ']'

        # 결과 반환
        return bridge_length, load_distribution, i_beam_spec, h_beam_spec, steel_material
