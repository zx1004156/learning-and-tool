import threading,sys,os,pickle
from panicBuying import PanicBuying
from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog,QLineEdit,QMessageBox,QTableWidgetItem
from PyQt5.QtCore import pyqtSignal,QObject,QDateTime,Qt
from PyQt5.QtGui import QIcon
from ui_main import Ui_MainWindow
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# -*- coding:utf-8 -*-

class Myignals(QObject):
    #定义一种信号,然后确定参数的类型
    log_add=pyqtSignal(str)

def init_window_main():
    global ui_main,window_main
    window_main.setWindowTitle('全能抢购神器2.2-请自觉关闭杀毒软件以免造成意外卡死!www.52pojie.cn')
    window_main.setWindowIcon(QIcon('logo.ico'))

    #加载数据
    load(dataPath)
    # 自动调节宽度
    ui_main.tab_mban.resizeColumnsToContents()
    #绑定按钮信号
    ui_main.bt_openWeb.clicked.connect(openWeb)
    ui_main.bt_start.clicked.connect(true_or_Flase)
    ui_main.bt_close_all.clicked.connect(reset)
    window_main.closeEvent=close
    ui_main.tab_mban.cellChanged.connect(cellChanged)
    ui_main.bt_add.clicked.connect(add_line)
    ui_main.bt_sub.clicked.connect(sub_line)

    ui_main.tab_mban.setAcceptDrops(True) # 设置接受拖放动作
    #ui_main.tab_mban.setDragEnabled(True)#支持主动拖动给别的控件
    #下方这三个事件必须同时重写
    ui_main.tab_mban.dragEnterEvent=dragEnterEvent#重写拖动输入事件
    ui_main.tab_mban.dragMoveEvent = dragMoveEvent#重写拖动鼠标移动事件
    ui_main.tab_mban.dropEvent=dropEvent#重写拖动松开事件


def dragEnterEvent(e):
    if e.mimeData().text().endswith('.pkl'):  # 拖拽过来如果是配置文件
        e.accept()
    else:
        e.ignore()

def dragMoveEvent(e):
    if e.mimeData().text().endswith('.pkl'):# 拖拽过来如果是配置文件
        e.setDropAction(Qt.MoveAction)
        e.accept()
    else:
        e.ignore()
def dropEvent(e):#松开鼠标得到路径
    print('sdgsgsd')
    path = e.mimeData().text().replace('file:///', '')  # 删除多余开头
    load(path)

def reset():
    global driver
    # 关闭所有的浏览器
    for item in driver:
        item.quit()
    close_all=True
    hw.start_kg = False
    ui_main.bt_start.setText('2.全部开始')
    driver=[]
    log_add('重置成功!')
def cellChanged(row, column):
    #自动调节宽度
    ui_main.tab_mban.resizeColumnsToContents()
def add_line():
    count=len(ui_main.tab_mban.selectedItems())

    if count > 0:
        #插入一行
        row = ui_main.tab_mban.currentRow()
        print(row)
        ui_main.tab_mban.insertRow(row)
    else:
        ui_main.tab_mban.setRowCount(ui_main.tab_mban.rowCount() + 1)
def sub_line():


    if ui_main.tab_mban.rowCount() > 0:
        count = len(ui_main.tab_mban.selectedItems())
        if count > 0:
            row = ui_main.tab_mban.currentRow()
            print(row)
            ui_main.tab_mban.removeRow(row)
        else:
            ui_main.tab_mban.setRowCount(ui_main.tab_mban.rowCount() - 1)
def load(path):
    '''
    读取配置项
    :return:
    '''
    try:

        with open(path,'rb')as f:
            setting = pickle.load(f)

        sets=setting['items']
        length = len(sets)
        print(setting)
        if length>0:
            #给这些控件初始化
            ui_main.ed_url.setText(setting['url'])

            ui_main.dte_time.setDateTime(QDateTime.fromString(setting['dte_time'],'hh:mm:ss'))
            ui_main.cb_sfds.setChecked(setting['cb_sfds'])
            ui_main.cb_tqsx.setChecked(setting['cb_tqsx'])
            #清空
            ui_main.tab_mban.clearContents()
            ui_main.tab_mban.setRowCount(length)
            ui_main.tab_mban.setColumnCount(3)
            print(sets)
            for i,im in enumerate(sets):
                store = QTableWidgetItem(im['store'])
                ui_main.tab_mban.setItem(i, 0, store)
                text=QTableWidgetItem(im['text'])
                ui_main.tab_mban.setItem(i, 1, text)
                css = QTableWidgetItem(im['css'])
                ui_main.tab_mban.setItem(i, 2, css)

    except Exception as err:
        print(err)
def save():
    '''
    保存配置项
    :return:
    '''
    items = []
    # 将表格的内容存在items中
    length = ui_main.tab_mban.rowCount()
    for i in range(length):
        try:

            items.append({'store': ui_main.tab_mban.item(i, 0).text(),
                          'text': ui_main.tab_mban.item(i, 1).text(),
                          'css': ui_main.tab_mban.item(i, 2).text()})

        except:
            pass
    setting={'items':items,
             'url':ui_main.ed_url.text(),
             'dte_time':ui_main.dte_time.text(),
             'cb_sfds':ui_main.cb_sfds.isChecked(),
             'cb_tqsx':ui_main.cb_tqsx.isChecked()}
    with open(dataPath, 'wb')as f:
        pickle.dump(setting, f)
    print(setting)
def close(enent):
    #关闭所有的浏览器
    for item in driver:
        item.quit()
    #保存数据
    save()
def openWeb():
    global driver,ms,close_all
    close_all = False
    #获取链接
    url=ui_main.ed_url.text()
    #获取设置的时间
    time_wait=ui_main.dte_time.text()
    #获取是否定时
    wait=ui_main.cb_sfds.isChecked()
    # 获取是否提前刷新
    refresh = ui_main.cb_tqsx.isChecked()

    # 创建浏览器
    try:
        driver.append(webdriver.Chrome())
    except:
        ui_main.ed_log.append('启动浏览器失败!请确定你的有安装谷歌浏览器和根目录有chromedriver.exe版本必须对应')
        ui_main.ed_log.append('浏览器下载:https://www.google.cn/chrome/')
        ui_main.ed_log.append('chromedriver下载:http://npm.taobao.org/mirrors/chromedriver/')
        ui_main.ed_log.append('【浏览器和这个驱动必须版本一致，可以根据版本去下载对应的驱动】')
        driver=[]
        return
    # 创建线程
    t.append(threading.Thread(target=hw.start,
                              args=(str(len(driver)),
                                    driver[-1],
                                    ms,
                                    url,
                                    ui_main.tab_mban,
                                    time_wait,
                                    wait,
                                    refresh)))
    # 设置主线程关闭时,它也跟着关闭
    t[-1].setDaemon(True)
    # 开始运行
    t[-1].start()
    ui_main.ed_log.append('现在请自己选择好产品的尺寸,规格,型号等参数,然后点全部开始,别关闭浏览器!')
def true_or_Flase():

    if len(driver)==0:
        log_add('请先增加浏览器')
        return
    if hw.start_kg==True:
        ui_main.bt_start.setText('2.全部开始')
        log_add('已经全部暂停!')
        hw.start_kg = False
    else:
        ui_main.bt_start.setText('2.全部暂停')

        log_add('已经全部开始!')
        hw.start_kg =True
def log_add(text):
    print(text)
    if text=='True':
        ui_main.bt_start.setText('2.全部暂停')
    else:
        ui_main.ed_log.append(text)
if __name__ == '__main__':
    dataPath='datas/set.pkl'
    # 自定义一个信号
    ms = log_sg = Myignals()
    # 绑定日志更新的信号
    ms.log_add.connect(log_add)
    #实例化抢购对象
    hw = PanicBuying()
    t = []#线程容器
    driver = []#浏览器容器
    start=False#全局暂停和开始的开关
    close_all=False
    app=QApplication(sys.argv)
    window_main = QMainWindow()  # 主界面
    ui_main = Ui_MainWindow()  # 实例化
    ui_main.setupUi(window_main)  # 运行里面的代码
    init_window_main()  # 初始化和对接代码功能
    with open('datas\main.qss', 'r',encoding='unicode_escape')as f:
        style = f.read()
    window_main.setStyleSheet(style)


    window_main.show()
    sys.exit(app.exec_())

