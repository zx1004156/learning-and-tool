# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.ed_log = QtWidgets.QTextEdit(self.centralwidget)
        self.ed_log.setMaximumSize(QtCore.QSize(300, 99999))
        self.ed_log.setObjectName("ed_log")
        self.gridLayout.addWidget(self.ed_log, 0, 5, 6, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uRLLabel = QtWidgets.QLabel(self.centralwidget)
        self.uRLLabel.setObjectName("uRLLabel")
        self.horizontalLayout_2.addWidget(self.uRLLabel)
        self.ed_url = QtWidgets.QLineEdit(self.centralwidget)
        self.ed_url.setObjectName("ed_url")
        self.horizontalLayout_2.addWidget(self.ed_url)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dte_time = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dte_time.setMinimumSize(QtCore.QSize(0, 0))
        self.dte_time.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dte_time.setTimeSpec(QtCore.Qt.LocalTime)
        self.dte_time.setObjectName("dte_time")
        self.horizontalLayout.addWidget(self.dte_time)
        self.cb_sfds = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_sfds.setObjectName("cb_sfds")
        self.horizontalLayout.addWidget(self.cb_sfds)
        self.cb_tqsx = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_tqsx.setObjectName("cb_tqsx")
        self.horizontalLayout.addWidget(self.cb_tqsx)
        self.bt_openWeb = QtWidgets.QPushButton(self.centralwidget)
        self.bt_openWeb.setMinimumSize(QtCore.QSize(80, 0))
        self.bt_openWeb.setObjectName("bt_openWeb")
        self.horizontalLayout.addWidget(self.bt_openWeb)
        self.bt_start = QtWidgets.QPushButton(self.centralwidget)
        self.bt_start.setMinimumSize(QtCore.QSize(80, 0))
        self.bt_start.setObjectName("bt_start")
        self.horizontalLayout.addWidget(self.bt_start)
        self.bt_close_all = QtWidgets.QPushButton(self.centralwidget)
        self.bt_close_all.setMinimumSize(QtCore.QSize(100, 0))
        self.bt_close_all.setObjectName("bt_close_all")
        self.horizontalLayout.addWidget(self.bt_close_all)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 4)
        self.te_help = QtWidgets.QTextEdit(self.centralwidget)
        self.te_help.setObjectName("te_help")
        self.gridLayout.addWidget(self.te_help, 5, 0, 1, 4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_an = QtWidgets.QLabel(self.centralwidget)
        self.lb_an.setObjectName("lb_an")
        self.horizontalLayout_3.addWidget(self.lb_an)
        self.bt_sub = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sub.setObjectName("bt_sub")
        self.horizontalLayout_3.addWidget(self.bt_sub)
        self.bt_add = QtWidgets.QPushButton(self.centralwidget)
        self.bt_add.setObjectName("bt_add")
        self.horizontalLayout_3.addWidget(self.bt_add)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 4)
        self.tab_mban = QtWidgets.QTableWidget(self.centralwidget)
        self.tab_mban.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tab_mban.setAcceptDrops(True)
        self.tab_mban.setObjectName("tab_mban")
        self.tab_mban.setColumnCount(3)
        self.tab_mban.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_mban.setItem(4, 2, item)
        self.gridLayout.addWidget(self.tab_mban, 4, 0, 1, 4)
        self.tab_mban.raise_()
        self.ed_log.raise_()
        self.te_help.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ed_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">日志:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请注意必须先设置好所有东西然后再去增加浏览器,不然设置会无效!</p></body></html>"))
        self.uRLLabel.setText(_translate("MainWindow", "目标链接:"))
        self.ed_url.setText(_translate("MainWindow", "https://www.vmall.com/product/10086726905036.html"))
        self.label.setText(_translate("MainWindow", "启动时间:"))
        self.dte_time.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">注意了,这里的时间是本地电脑的时间</span></p><p><br/></p><p><span style=\" font-size:11pt;\">提前刷新是会在时间到的时候先刷新然后再开始</span></p><p><br/></p><p><span style=\" font-size:11pt;\">(如果太晚了,可以时间稍微提前一点)</span></p></body></html>"))
        self.dte_time.setDisplayFormat(_translate("MainWindow", "hh:mm:ss.zzz"))
        self.cb_sfds.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">注意了,这里的时间是本地电脑的时间</span></p><p><br/></p><p><span style=\" font-size:11pt;\">提前刷新是会在时间到的时候先刷新然后再开始</span></p><p><br/></p><p><span style=\" font-size:11pt;\">(如果太晚了,可以时间稍微提前一点)</span></p></body></html>"))
        self.cb_sfds.setText(_translate("MainWindow", "定时启动"))
        self.cb_tqsx.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">注意了,这里的时间是本地电脑的时间</span></p><p><br/></p><p><span style=\" font-size:11pt;\">提前刷新是会在时间到的时候先刷新然后再开始</span></p><p><br/></p><p><span style=\" font-size:11pt;\">(如果太晚了,可以时间稍微提前一点)</span></p></body></html>"))
        self.cb_tqsx.setText(_translate("MainWindow", "提前刷新"))
        self.bt_openWeb.setText(_translate("MainWindow", "1.增加浏览器"))
        self.bt_start.setText(_translate("MainWindow", "2.全部开始"))
        self.bt_close_all.setText(_translate("MainWindow", "3.关闭所有浏览器"))
        self.te_help.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-weight:600;\">使用步骤: </span><span style=\" font-family:\'微软雅黑\'; font-weight:600; color:#ffaa00;\">欢迎在论坛留言分享你的配置（支持将pkl配置文件拖动到列表中完全一键读取）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:600; color:#ff0000;\">演示视频</span><a href=\"https://www.bilibili.com/video/BV1S54y147xc\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.bilibili.com/video/BV1S54y147xc</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:600; color:#ff0000;\">网友分享</span><a href=\"https://lanren.lanzous.com/b00u4meta \"><span style=\" text-decoration: underline; color:#0000ff;\">https://lanren.lanzous.com/b00u4meta </span></a><span style=\" font-family:\'微软雅黑\'; font-size:12pt; color:#0000ff;\">密码:lanren</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-weight:600; color:#0000ff;\">本工具不仅仅可用来抢购，更是一个浏览器自动化傻瓜式设计脚本，可用来随意控制多个浏览器</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">1. 点击[</span><span style=\" font-family:\'微软雅黑\'; font-weight:600; color:#ff0000;\">增加浏览器</span><span style=\" font-family:\'微软雅黑\';\">]就是多增加一个浏览器（</span><span style=\" font-family:\'微软雅黑\'; font-weight:600; color:#ff0000;\">注意，不能出现多个页面，一个浏览器就一个页面</span><span style=\" font-family:\'微软雅黑\';\">）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">2. 在浏览器中登录你的账号,并把产品的尺寸,规格,型号等参数手动弄好!</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">3. 设置好一切后,点击[</span><span style=\" font-family:\'微软雅黑\'; font-weight:600; color:#ff0000;\">全部开始</span><span style=\" font-family:\'微软雅黑\';\">]</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-weight:600; color:#ff0000;\">为了让大家能理解,给大家说下软件的工作原理:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">1. 原理就是多开浏览器,然后脚本同步进行控制</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">2. 当点击全部开始后它就会根据你填写的目标按钮以及Css选择器作为定位目标按钮的依据</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">3. 优先CSS选择器(下方有教程),如果没找到,则会通过目标按钮名来定位目标按钮</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">4. 只需要满足其中一个条件就可以找到目标,然后就会不断点击</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">5.支持判断N个按钮,比如你的购买步骤比较多时,只要提前加入好目标按钮名和选择器就可以骚气运行</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">6.支持帮忙输入文字的操作,比如帮忙输入密码</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">7.它是按照顺序往下走的(注意了我特意改进了一下)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-weight:600;\">如何填写目标按钮 和 CSS选择器呢?</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-weight:600;\">目标名:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">目标按钮名,很容易理解就是你需要帮忙点击的按钮的标题(必须是可以开始抢购时的按钮名)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">如果是需要输入文字,则这里的填写格式为$$文字 比如:$$123456 它就会输入123456</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#ff0000;\">如果是选择帮忙输入了,那就只能用CSS选择器的方式定位输入框</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:600; color:#0000ff;\">进阶玩法:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-size:11pt; color:#ff0000;\">这里的目标按钮支持前缀%% 来控制不重复点击 ##来配置下拉滚动条 可以同时存在</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">1.一开始是灰色的按钮,或者点击后马上就跳转到下一个页面的就不需要前缀%%</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">2.如果是随时就可以点击成功的按钮,则在前面加入%%</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">例如:</span><span style=\" color:#0000ff;\">%%加入购物车 </span><span style=\" color:#ffaa00;\">%%预约</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#000000;\">3.如果跳转后目标按钮并没有第一时间渲染显示,需要下划滚动条,则在目标按钮名字中随便一个位置加入##来标识</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">例如</span><span style=\" font-family:\'微软雅黑\'; color:#000000;\">:京东的提交订单 可以这样填:</span><span style=\" font-family:\'微软雅黑\'; color:#ff0000;\">##提交订单</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#000000;\">4.如果您需要程序暂时等待N秒 然后再执行，可以添加一行 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#000000;\">例如 ：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#000000;\">    第二列中写入（就是 目标按钮/输入框/等待栏目）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#000000;\">    等待xx秒  例如 ：等待5秒 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; color:#ff0000;\">原理解析:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">因为正常情况下,程序是会不断的去点击目标按钮的直到整个按钮不见了,程序才会往下走,去判断下一个步骤,比如淘宝的立即购买,一开始是没有这个按钮的,或者是点不动的,只有到时间了才能点击,点击后,直接是调到提交订单的页面了,也就是这个立即购买按钮已经消失了,所以程序会执行下一步,而这个%%就是不判断是否点击成功,反正就找到这个按钮了,就帮忙点击1次,没找到就等待它出现.点完后就开始下一个步骤!仔细理解一下就明白区别了!</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\'; font-weight:600;\">目标CSS选择器:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">(1) 首先用Google Chrome浏览器打开你的商品网站</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">(2) 然后按下F12进入开发者模式</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">(3) 然后看图操作</span><a href=\"https://attach.52pojie.cn//forum/202011/12/165648ml2jxid0bzflaz0f.gif\"><span style=\" text-decoration: underline; color:#0000ff;\">https://attach.52pojie.cn//forum/202011/12/165648ml2jxid0bzflaz0f.gif</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lb_an.setText(_translate("MainWindow", "点击目标:(这里可以添加N个按钮目标,只要网页里出现了它,就会帮忙点击)"))
        self.bt_sub.setText(_translate("MainWindow", "删除一行"))
        self.bt_add.setText(_translate("MainWindow", "添加一行"))
        self.tab_mban.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ff0000;\">这里请注意了: </span></p><p><span style=\" font-size:11pt;\">如果是要输入 注意前缀格式</span><span style=\" font-size:11pt; color:#0000ff;\">$$</span><span style=\" font-size:11pt;\">:</span></p><p><span style=\" font-size:11pt;\">比如:</span><span style=\" font-size:11pt; color:#0000ff;\"> $$123456 </span></p><p><span style=\" font-size:11pt;\">那它就会输入</span><span style=\" font-size:11pt; color:#ffaa00;\">123456</span></p><p><span style=\" font-size:11pt; font-weight:600;\">注意这里如果是填的输入,那CSS就必须设置</span></p><p><span style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:600; color:#0000ff;\">进阶玩法:</span></p><p><span style=\" font-family:\'微软雅黑\'; font-size:11pt; color:#ff0000;\">这里的目标按钮支持前缀%% 来控制不重复点击 ##来配置下拉滚动条 可以同时存在</span></p><p><span style=\" font-family:\'微软雅黑\';\">1.一开始是灰色的按钮,或者点击后马上就跳转到下一个页面的就不需要前缀%%</span></p><p><span style=\" font-family:\'微软雅黑\';\">2.如果是随时就可以点击成功的按钮,则在前面加入%%</span></p><p><span style=\" font-family:\'微软雅黑\';\">例如:</span><span style=\" font-family:\'SimSun\'; color:#0000ff;\">%%加入购物车 </span><span style=\" font-family:\'SimSun\'; color:#ffaa00;\">%%预约</span></p><p><span style=\" font-family:\'微软雅黑\'; color:#000000;\">3.如果跳转后目标按钮并没有第一时间渲染显示,需要下划滚动条,则在目标按钮名字中随便一个位置加入##来标识</span></p><p><span style=\" font-family:\'微软雅黑\';\">例如</span><span style=\" font-family:\'微软雅黑\'; color:#000000;\">:京东的提交订单 可以这样填:</span><span style=\" font-family:\'微软雅黑\'; color:#ff0000;\">##提交订单</span></p><p><span style=\" font-family:\'微软雅黑\'; color:#000000;\">4.如果您需要程序暂时等待N秒 然后再执行，可以添加一行 </span></p><p><span style=\" font-family:\'微软雅黑\'; color:#000000;\">例如 ：</span></p><p><span style=\" font-family:\'微软雅黑\'; color:#000000;\">    第二列中写入（就是 目标按钮/输入框/等待栏目）</span></p><p><span style=\" font-family:\'微软雅黑\'; color:#000000;\">    等待xx秒  例如 ：等待5秒 </span></p><p><span style=\" font-family:\'微软雅黑\'; color:#ff0000;\">原理解析:</span></p><p><span style=\" font-family:\'微软雅黑\';\">因为正常情况下,程序是会不断的去点击目标按钮的直到整个按钮不见了,程序才会往下走,去判断下一个步骤,比如淘宝的立即购买,一开始是没有这个按钮的,或者是点不动的,只有到时间了才能点击,点击后,直接是调到提交订单的页面了,也就是这个立即购买按钮已经消失了,所以程序会执行下一步,而这个%%就是不判断是否点击成功,反正就找到这个按钮了,就帮忙点击1次,没找到就等待它出现.点完后就开始下一个步骤!仔细理解一下就明白区别了!</span></p></body></html>"))
        item = self.tab_mban.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tab_mban.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tab_mban.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tab_mban.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tab_mban.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tab_mban.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "备注(不影响脚本)"))
        item = self.tab_mban.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "目标按钮/输入框/等待"))
        item = self.tab_mban.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "目标CSS选择器"))
        __sortingEnabled = self.tab_mban.isSortingEnabled()
        self.tab_mban.setSortingEnabled(False)
        item = self.tab_mban.item(0, 0)
        item.setText(_translate("MainWindow", "不断点击它，直到成功"))
        item = self.tab_mban.item(0, 1)
        item.setText(_translate("MainWindow", "立即购买"))
        item = self.tab_mban.item(0, 2)
        item.setText(_translate("MainWindow", "#J_LinkBuy"))
        item = self.tab_mban.item(1, 0)
        item.setText(_translate("MainWindow", "如果你要程序等待N秒"))
        item = self.tab_mban.item(1, 1)
        item.setText(_translate("MainWindow", "等待5秒"))
        item = self.tab_mban.item(2, 0)
        item.setText(_translate("MainWindow", "点击一次，不管是否成功"))
        item = self.tab_mban.item(2, 1)
        item.setText(_translate("MainWindow", "%%提交订单"))
        item = self.tab_mban.item(2, 2)
        item.setText(_translate("MainWindow", "#submitOrderPC_1 > div > a"))
        item = self.tab_mban.item(3, 0)
        item.setText(_translate("MainWindow", "输入密码"))
        item = self.tab_mban.item(3, 1)
        item.setText(_translate("MainWindow", "$$123456"))
        item = self.tab_mban.item(3, 2)
        item.setText(_translate("MainWindow", "#payPassword_rsainput"))
        item = self.tab_mban.item(4, 0)
        item.setText(_translate("MainWindow", "点击一次，并且加载全部页面内容"))
        item = self.tab_mban.item(4, 1)
        item.setText(_translate("MainWindow", "##%%确认付款"))
        item = self.tab_mban.item(4, 2)
        item.setText(_translate("MainWindow", "#J_authSubmit"))
        self.tab_mban.setSortingEnabled(__sortingEnabled)
