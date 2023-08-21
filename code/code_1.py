
from tkinter import *
import time

LOG_LINE_NUM = 0

# HEX数字列表转ASCII




class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("狮子工具箱")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="输入数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)

        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)

        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)

        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="开始转换", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)



    

    #功能函数
    def str_trans_to_md5(self):
        #输入的十六进制字符串转化为十六进制字符列表
        srcList = self.init_data_Text.get(1.0,END).strip().replace("\n","").split()

        
        if srcList:
            try:

                #十六进制字符列表转化为数字列表
                hexList = [ int(x,16) for x in srcList]
                print('hexList is ',hexList)

                #计算hexList长度
                hexListLen = len(hexList)
                print('the length of the list is :',hexListLen)

                #寻找2C进行列表分割
                # comma_index=hexList.index(0x2c)
                # print(comma_index)
                

                
                # 准备接收列表
                hexListBegin=[]
                hexListBeginString=""

                hexListImei=[]
                hexListProt=[]

                #用于承接后面的暂时列表变量
                hexListTemp=[] 


                hexListBegin = hexList[0:hexList.index(0x2c)]

                BeginStringList=[chr(i) for i in hexListBegin[:2]]
                BeginString="".join(BeginStringList)

                identSignString = chr(hexListBegin[2])

                packLenStringList = [chr(i) for i in hexListBegin[3:len(hexListBegin)]]
                packLenString = "".join(packLenStringList)
                




                hexListTemp = hexList[hexList.index(0x2c)+1:-1] #+1 是删除逗号

                hexListImei = hexListTemp[0:hexListTemp.index(0x2c)]

                hexListImeiStringList = [chr(i) for i in hexListImei]
                hexListImeiString = "".join(hexListImeiStringList) #IMEI字符串

                hexListTemp = hexListTemp[hexListTemp.index(0x2c)+1:-1]

                hexListProt = hexListTemp[0:hexListTemp.index(0x2c)]
                hexListProtStringList = [chr(i) for i in hexListProt]
                hexListProtString = "".join(hexListProtStringList) #IMEI字符串

                hexListTemp = hexListTemp[hexListTemp.index(0x2c)+1:-1]

                hexListBeginString="数据包开始标志为：" + BeginString + "\r\n"\
                                   "数据包标识符为：" + identSignString + "\r\n"\
                                   "数据长度为：" + packLenString + "\r\n"\
                                   "设备IMEI号为：" + hexListImeiString + "\r\n"\
                                   "设备数据包协议为：" + hexListProtString + "\r\n"

                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"初始数据列表是:\r\n")
                self.result_data_Text.insert(2.0,srcList)
                self.result_data_Text.insert(3.0,"\r\n")
                self.result_data_Text.insert(4.0, hexListBeginString)




                self.write_log_to_Text("INFO:str_trans_to_md5 success")

            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()