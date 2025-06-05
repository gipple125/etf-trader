import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 작동 테스트")
window.setGeometry(100, 100, 300, 100)

layout = QVBoxLayout()
label = QLabel("🎉 PyQt5가 정상 작동하고 있습니다!")
layout.addWidget(label)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
