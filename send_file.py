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
image = Image.open('./demo.gif') # https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA18ibV9.img

# 将图片转换为RGB模式
image = image.convert('RGB')

# 获取图像数据
image_data = list(image.getdata())

# 获取图像大小
image_size = image.size

# 将图像数据转换为字节数组
byte_data = bytearray([c for p in image_data for c in p])

# 将 JPEG 图片转换为 CF_DIB 格式
output = io.BytesIO()
image.convert('RGB').save(output, 'BMP')
data = output.getvalue()[14:]
output.close()

# 文件地址
file_path = './text.txt'

# 将文件路径放到文件列表中
file_list = [file_path]

# 将文件列表打包成适合 CF_HDROP 数据格式的字节数组
file_bytes = '\0'.join(file_list).encode('utf-8') + b'\0\0'

# 将文件路径复制到系统剪贴板中(没效果)
# pyperclip.copy(file_path)



def get_msg_list():
    msg_list = [] # 找到窗口的list部件然后获取句柄
    msg_ctrl_list = spying_window.ListControl().GetChildren()
    for msg_ctrl in msg_ctrl_list:
        msg_list.append(msg_ctrl.Name)
    return msg_list

def send_img_msg():
    # 将文件列表复制到剪贴板
    # win32clipboard.OpenClipboard()
    # win32clipboard.EmptyClipboard()
    # print(image)
    # # win32clipboard.SetClipboardData(win32clipboard.CF_DIB, image.tobytes())
    # win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    # win32clipboard.CloseClipboard()
    time.sleep(5)
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