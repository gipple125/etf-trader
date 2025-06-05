import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QAxContainer import QAxWidget
from db.db_manager import insert_etf_price
import sys

class ETFPriceReceiver(QMainWindow):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self.indi = QAxWidget("GIEXPERTCONTROL.GiExpertControlCtrl.1")
        self.indi.ReceiveRTData.connect(self.receive_rt_data)

        # 실시간 현재가 등록 (SC는 현물 현재가 TR코드)
        self.indi.dynamicCall("RequestRTReg(QString, QString)", "SC", self.symbol)

    def receive_rt_data(self, RealType):
        if RealType == "SC":
            price = self.indi.dynamicCall("GetSingleData(int)", 3)  # 현재가
            time = self.indi.dynamicCall("GetSingleData(int)", 2)   # 시간
            print(f"[{self.symbol}] 시세: {price} / 시각: {time}")

            # DB에 저장
            insert_etf_price(symbol=self.symbol, price=price, time=time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    receiver = ETFPriceReceiver("069500")  # 예: KODEX 200
    receiver.show()
    sys.exit(app.exec_())
