import uiautomation
import time
from translate import Translator

#定位微信主窗口，获取窗口句辆
spying_window_name ="wx_demo3"
spying_window = uiautomation.WindowControl(searchDepth=1, Name=spying_window_name)

def get_msg_list():
    msg_list = [] # 找到窗口的list部件然后获取句柄
    print(spying_window)
    msg_ctrl_list = spying_window.ListControl().GetChildren()
    print(msg_ctrl_list)
    for msg_ctrl in msg_ctrl_list:
        msg_list.append(msg_ctrl.Name)
    return msg_list

def send_text_msg(text_msg):
    spying_window.SendKeys(text_msg) # 写入消息
    spying_window.SendKey(13) # 点击Enter按键

tran_to_chinese = Translator(from_lang='en', to_lang='zh')
tran_to_english = Translator(from_lang='zh', to_lang='en')

def auto_translate(input_content):
    return input_content
    for letter in input_content:
        if '\u4e00'<= letter <= '\u9fff': # 判断是否中文
            return tran_to_english.translate(input_content)
        else:
            return tran_to_chinese.translate(input_content)

former_msg_list = get_msg_list()    # 上一条消息
while True:
    latest_msg_list = get_msg_list()
    if latest_msg_list != former_msg_list: # 当未条消息和上一条消息不同时
        new_msg = latest_msg_list[-1]
        print(new_msg)
        #----- new_msg就是新的消息----- #
        text = auto_translate(new_msg)
        print(text)
        send_text_msg(text)
        # -=--
        former_msg_list = get_msg_list()
        time.sleep(5)