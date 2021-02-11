'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-24 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
from umqtt import MQTTClient
import utime
import log
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_MQTT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")



state = 0

def sub_cb(topic, msg):
    global state
    mqtt_log.info("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
    state = 1


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

    # 创建一个mqtt实例
    c = MQTTClient("umqtt_client", "mq.tongxinmao.com", 18830)
    # 设置消息回调
    c.set_callback(sub_cb)
    #建立连接
    c.connect()
    # 订阅主题
    c.subscribe(b"/public/TEST/quecpython")
    mqtt_log.info("Connected to mq.tongxinmao.com, subscribed to /public/TEST/quecpython topic" )
    # 发布消息
    c.publish(b"/public/TEST/quecpython", b"my name is Quecpython!")
    mqtt_log.info("Publish topic: /public/TEST/quecpython, msg: my name is Quecpython")

    while True:
        c.wait_msg()  # 阻塞函数，监听消息
        if state == 1:
            break

    # 关闭连接
    c.disconnect()