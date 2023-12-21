import uiautomation
import uiautomation as automation
import time
from translate import Translator
from PIL import Image
import io
# import pyperclip
import win32clipboard
import win32con


#定位微信主窗口，获取窗口句辆
spying_window_name ="wx_demo3"
spying_window = uiautomation.WindowControl(searchDepth=1, Name=spying_window_name)

# 加载图片
# image = Image.open('./image.jpg')
image = Image.open('https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA18ibV9.img') # https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA18ibV9.img

# 将 JPEG 图片转换为 CF_DIB 格式
output = io.BytesIO()
image.convert('RGB').save(output, 'BMP')
data = output.getvalue()[14:]
output.close()



def get_msg_list():
    msg_list = [] # 找到窗口的list部件然后获取句柄
    msg_ctrl_list = spying_window.ListControl().GetChildren()
    for msg_ctrl in msg_ctrl_list:
        msg_list.append(msg_ctrl.Name)
    return msg_list

def send_img_msg():
    # 将文件列表复制到剪贴板
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    print(image)
    # win32clipboard.SetClipboardData(win32clipboard.CF_DIB, image.tobytes())
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
    spying_window.SendKeys('{Ctrl}v') # 按下 Ctrl + V 快捷键，粘贴文件路径
    spying_window.SendKey(13) # 点击Enter按键

former_msg_list = get_msg_list()    # 上一条消息
while True:
    latest_msg_list = get_msg_list()
    if latest_msg_list != former_msg_list: # 当未条消息和上一条消息不同时
        new_msg = latest_msg_list[-1]
        print(new_msg)
        send_img_msg()
        # -=--
        former_msg_list = get_msg_list()
        time.sleep(5)