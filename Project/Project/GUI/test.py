import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6 import uic
from PyQt6.QtGui import QPixmap

# 현재 파일의 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))

# UI 파일 경로 설정
ui_path = os.path.join(current_dir, 'GUI_image.ui')

# UI 파일 로드
form_class, base_class = uic.loadUiType(ui_path)

class ImageWindow(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_images()

    def load_images(self):
        # I형강.png와 H형강.png 파일의 절대 경로 설정
        i_image_path = os.path.join(current_dir, 'I형강.png')
        h_image_path = os.path.join(current_dir, 'H형강.png')

        # 경로를 출력하여 확인
        print(f"I형강 경로: {i_image_path}")
        print(f"H형강 경로: {h_image_path}")

        # QLabel을 사용하여 이미지를 로드
        pixmap_i = QPixmap(i_image_path)
        pixmap_h = QPixmap(h_image_path)

        self.label_i = QLabel(self)
        self.label_i.setPixmap(pixmap_i)
        self.label_i.setGeometry(10, 10, pixmap_i.width(), pixmap_i.height())

        self.label_h = QLabel(self)
        self.label_h.setPixmap(pixmap_h)
        self.label_h.setGeometry(300, 10, pixmap_h.width(), pixmap_h.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()
    sys.exit(app.exec())
