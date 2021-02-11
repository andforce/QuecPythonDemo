from TenCentYun import TXyun
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_TencentYun_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
txyun_log = log.getLogger("TenCentYun")

'''
腾讯云物联网套件客户端功能
'''
productID = ""  # 产品标识（参照接入腾讯云应用开发指导）
devicename = ""   # 设备名称（参照接入腾讯云应用开发指导）
devicePsk = ""   # 设备密钥（一型一密认证此参数传入None， 参照接入腾讯云应用开发指导）
ProductSecret = None   # 产品密钥（一机一密认证此参数传入None，参照接入腾讯云应用开发指导）

tenxun = TXyun(productID, devicename, devicePsk, ProductSecret)  # 创建连接对象
state = 5

def sub_cb(topic, msg):   # 云端消息响应回调函数
    global state
    txyun_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state -= 1


if __name__ == '__main__':
    '''
    手动运行本例程时，可以去掉该延时，如果将例程文件名改为main.py，希望开机自动运行时，需要加上该延时,
    否则无法从CDC口看到下面的 poweron_print_once() 中打印的信息
    '''
    utime.sleep(5)
    checknet.poweron_print_once()
    '''
    如果用户程序包含网络相关代码，必须执行 wait_network_connected() 等待网络就绪（拨号成功）；
    如果是网络无关代码，可以屏蔽 wait_network_connected()
    【本例程必须保留下面这一行！】
    '''
    checknet.wait_network_connected()

    tenxun.setMqtt()  # 设置mqtt
    tenxun.setCallback(sub_cb)   # 设置消息回调函数
    topic = ""  # 输入自定义的Topic
    tenxun.subscribe(topic)   # 订阅Topic
    tenxun.start()
    tenxun.publish(topic, "hello world")   # 发布消息

    while 1:
        if state:
            pass
        else:
            tenxun.disconnect()
            break
