'''
@Author: Pawn
@Date: 2020-08-12
@LastEditTime: 2020-08-12 17:06:08
@Description: example for module timer
@FilePath: example_wdt.py
'''

from machine import WDT
from machine import Timer
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_WDT_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

timer1 = Timer(Timer.Timer1)

def feed(t):
    wdt.feed()


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
    【本例程可以屏蔽下面这一行！】
    '''
    # checknet.wait_network_connected()

    wdt = WDT(20)  # 启动看门狗，间隔时长
    timer1.start(period=15000, mode=timer1.PERIODIC, callback=feed)  # 使用定时器喂狗

    # wdt.stop()
