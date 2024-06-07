import os
import sys
import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QWidget, QVBoxLayout, QButtonGroup, QMessageBox
from PyQt6 import uic
from openpyxl import load_workbook
import os
print("Current Working Directory:", os.getcwd())

# # 바탕화면의 절대 경로 설정
# desktop_path = r'C:\Users\pcy45\OneDrive\바탕 화면\GUI_test.ui'
# excel_path = r'C:\Users\pcy45\OneDrive\바탕 화면\database.xlsx'
# .ui 파일 로드
# form_class, base_class = uic.loadUiType(desktop_path)

# 상대경로 설정
# 현재 폴더 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# 현재 폴더에 있는 GUI_test.ui 파일 경로
desktop_path = os.path.join(current_dir, 'GUI_test.ui')
image_ui_path = os.path.join(current_dir, 'GUI_image.ui')
# 현재 폴더의 상위 폴더에 있는 Database 폴더에 있는 database.xlsx 파일 경로
excel_path = os.path.join(current_dir, '..', 'Database', 'database.xlsx')
# .ui 파일 로드
form_class, base_class = uic.loadUiType(desktop_path)
image_form_class, image_base_class = uic.loadUiType(image_ui_path)

class ImageWindow(QWidget, image_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_radio_object_name = None
        self.image_window = None
        self.add_radio_buttons_to_select_column()
        self.add_other_radio_buttons()
        self.setup_validators()
        self.disable_table_editing()

        # 정확한 객체 이름으로 변경
        self.pushButton.clicked.connect(self.save_data)

        # image_button 클릭 시 GUI_image.ui 파일을 로드하는 창을 엽니다.
        self.image_button.clicked.connect(self.open_image_window)

    def add_radio_buttons_to_select_column(self):
        self.buttonGroup_I = QButtonGroup(self)
        self.buttonGroup_I.setExclusive(True)

        self.buttonGroup_H = QButtonGroup(self)
        self.buttonGroup_H.setExclusive(True)

        # I-beam 선택 열에 라디오 버튼 추가
        rows_i = self.tableWidget_I.rowCount()
        column_i = 5  # I-beam 선택 열의 인덱스 (0부터 시작)

        for row in range(rows_i):
            radio_button = QRadioButton()
            radio_button.setObjectName(f"radio_I_{row}")
            self.buttonGroup_I.addButton(radio_button)
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(radio_button)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.tableWidget_I.setCellWidget(row, column_i, widget)
            radio_button.clicked.connect(self.store_selected_radio_object_name)

        # H-beam 선택 열에 라디오 버튼 추가
        rows_h = self.tableWidget_H.rowCount()
        column_h = 4  # H-beam 선택 열의 인덱스 (0부터 시작)

        for row in range(rows_h):
            radio_button = QRadioButton()
            radio_button.setObjectName(f"radio_H_{row}")
            self.buttonGroup_H.addButton(radio_button)
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.addWidget(radio_button)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.tableWidget_H.setCellWidget(row, column_h, widget)
            radio_button.clicked.connect(self.store_selected_radio_object_name)

    def add_other_radio_buttons(self):
        self.buttonGroup_Other = QButtonGroup(self)
        self.buttonGroup_Other.setExclusive(True)  # "그 외" 라디오 버튼 그룹도 단일 선택으로 설정

        # "그 외" 라디오 버튼 추가
        radio_button_names = ["SS235", "SS275", "SS315", "SS410", "SS450", "SS550"]

        for name in radio_button_names:
            radio_button = self.findChild(QRadioButton, name)
            if radio_button:
                self.buttonGroup_Other.addButton(radio_button)
                radio_button.clicked.connect(self.store_selected_other_radio_object_name)

    def store_selected_radio_object_name(self):
        sender = self.sender()  # 클릭된 QRadioButton을 가져옵니다

        if sender.isChecked():
            self.selected_radio_object_name = sender.objectName()
        else:
            self.selected_radio_object_name = None

        self.disable_other_group()

    def store_selected_other_radio_object_name(self):
        sender = self.sender()  # 클릭된 QRadioButton을 가져옵니다

        if sender.isChecked():
            self.selected_radio_object_name = sender.objectName()
        else:
            self.selected_radio_object_name = None
        # 다른 그룹을 비활성화하지 않음

    def disable_other_group(self):
        # I-beam에서 선택하면 H-beam을 비활성화
        any_i_checked = any(radio_button.isChecked() for radio_button in self.buttonGroup_I.buttons())
        any_h_checked = any(radio_button.isChecked() for radio_button in self.buttonGroup_H.buttons())

        if any_i_checked:
            for rb in self.buttonGroup_H.buttons():
                rb.setEnabled(False)
        elif any_h_checked:
            for rb in self.buttonGroup_I.buttons():
                rb.setEnabled(False)
        else:
            for rb in self.buttonGroup_I.buttons():
                rb.setEnabled(True)
            for rb in self.buttonGroup_H.buttons():
                rb.setEnabled(True)

    def setup_validators(self):
        int_validator = QIntValidator(0, 1000000, self)
        self.length.setValidator(int_validator)
        self.weight.setValidator(int_validator)

    def disable_table_editing(self):
        # 모든 테이블 셀을 읽기 전용으로 설정
        for row in range(self.tableWidget_I.rowCount()):
            for column in range(self.tableWidget_I.columnCount()):
                item = self.tableWidget_I.item(row, column)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

        for row in range(self.tableWidget_H.rowCount()):
            for column in range(self.tableWidget_H.columnCount()):
                item = self.tableWidget_H.item(row, column)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

    def save_data(self):
        length = self.length.text()
        weight = self.weight.text()
        combobox_value = self.comboBox.currentText()
        combobox_2_value = self.comboBox_2.currentText()

        selected_radio_i = None
        selected_row_i = None
        for row, radio_button in enumerate(self.buttonGroup_I.buttons()):
            if radio_button.isChecked():
                selected_radio_i = radio_button.objectName()
                selected_row_i = row
                break

        selected_radio_h = None
        selected_row_h = None
        for row, radio_button in enumerate(self.buttonGroup_H.buttons()):
            if radio_button.isChecked():
                selected_radio_h = radio_button.objectName()
                selected_row_h = row
                break

        if selected_row_i is not None:
            row_values_i = [
                self.tableWidget_I.item(selected_row_i, col).text() if self.tableWidget_I.item(selected_row_i,
                                                                                               col) else '' for col in
                range(self.tableWidget_I.columnCount())]
        else:
            row_values_i = [None] * self.tableWidget_I.columnCount()

        if selected_row_h is not None:
            row_values_h = [
                self.tableWidget_H.item(selected_row_h, col).text() if self.tableWidget_H.item(selected_row_h,
                                                                                               col) else '' for col in
                range(self.tableWidget_H.columnCount())]
        else:
            row_values_h = [None] * self.tableWidget_H.columnCount()

        data = {
            'Length': [length],
            'ComboBox': [combobox_value],
            'Weight': [weight],
            'ComboBox_2': [combobox_2_value],
            # 'Selected I-Beam': [selected_radio_i],
            'I-Beam Row Values': [row_values_i],
            # 'Selected H-Beam': [selected_radio_h],
            'H-Beam Row Values': [row_values_h],
            'Selected Radio Object Name': [self.selected_radio_object_name]
        }

        df = pd.DataFrame(data)

        try:
            with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='input', index=False, header=False,
                            startrow=writer.sheets['input'].max_row)
        except FileNotFoundError:
            df.to_excel(excel_path, sheet_name='input', index=False)

        QMessageBox.information(self, "입력완료!", "트러스 구조 설계를 시작합니다.")

    def open_image_window(self):
        if self.image_window is None:
            self.image_window = ImageWindow()
        self.image_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec())