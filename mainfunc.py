import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from card_draw import Ui_Form

import numpy as np



class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        
        #更改标题
        self.setWindowTitle('抽卡模拟器')
        
        #添加单抽按钮信号和槽
        self.one_draw.clicked.connect(self.one)
        
        #添加十连按钮信号和槽
        self.ten_draw.clicked.connect(self.ten)
     
    def one(self):
        data = []
        # 一行行读取角色数据
        for line in open('C://Users//熊天昊//Desktop//VSC File//card_draw//card_data.txt','r'):
            data.append(line)
        
        ##分离4星和5星卡池
        data_4 = []
        data_5 = []
        for i in range(0,len(data)):
            if ('4星' in data[i]):
                data_4.append(data[i])
            else:
                data_5.append(data[i])
        
        #读取5星概率
        prob = self.prob.text()


        #设置抽到的卡牌等级，之后随机抽一张卡，并改变保底次数
        count_num = self.count.text()
        num = count_num.split('>')[5].split('<')[0]
        if (int(num) - 1 > 0):
            self.count.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">' + str(int(num) - 1) + '</span></p></body></html>')

            p = np.random.rand()

            if (p <= float(prob)/100):
                self.count.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">80</span></p></body></html>')
                num = np.random.randint(0,len(data_5))
                card = data_5[num]
            else:
                num = np.random.randint(0,len(data_4))
                card = data_4[num]

        else:
            self.count.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">80</span></p></body></html>')
            num = np.random.randint(0,len(data_5))
            card = data_5[num]
            
        #输出结果
        self.result.setText('恭喜你抽到了：' + card)

    def ten(self):
        data = []
        # 一行行读取角色数据
        for line in open('C://Users//熊天昊//Desktop//VSC File//card_draw//card_data.txt','r'):
            data.append(line)
        
        #分离4星和5星卡池
        data_4 = []
        data_5 = []
        for i in range(0,len(data)):
            if ('4星' in data[i]):
                data_4.append(data[i])
            else:
                data_5.append(data[i])
        
        #定义之后要输出的文本
        text = '恭喜你抽到了：\n'

        #读取5星概率
        prob = self.prob.text()

        for i in range(0,10):
            #改变保底次数
            count_num = self.count.text()
            num = count_num.split('>')[5].split('<')[0]
            if (int(num) - 1 > 0):
                self.count.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">' + str(int(num) - 1) + '</span></p></body></html>')

                p = np.random.rand()

                if (p <= float(prob)/100):
                    self.count.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">80</span></p></body></html>')
                    num = np.random.randint(0,len(data_5))
                    card = data_5[num]
                else:
                    num = np.random.randint(0,len(data_4))
                    card = data_4[num]

                text = text + card

            else:
                self.count.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">80</span></p></body></html>')
                num = np.random.randint(0,len(data_5))
                card = data_5[num]
                text = text + card
                continue
            
        #输出结果
        self.result.setText(text)
        
            

    
    

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())