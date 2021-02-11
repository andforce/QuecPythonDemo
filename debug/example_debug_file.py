# -*- coding: UTF-8 -*-

"""
本例程以main.py程序为基础，添加了debug相关示例
主要是通过定时器周期打印一些关键的系统信息，输出到CDC口,
输出的信息有：当前可用ram、rom、电池电压以及信号强度
用户可根据需要调整打印周期，当前设置为30s打印一次，最短不能低于5ms
"""

import gc
import net
import log
import utime
import osTimer
import _thread
import checkNet
from misc import Power


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Debug_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

log.basicConfig(level=log.DEBUG)
cdc_log = log.getLogger("Log")

# 创建系统定时器对象
ostimer = osTimer()


'''
此函数循环（间隔30s）打印，用于输出模块信息，便于了解模块运行状态
如果不需要，请注释调定时器timer
'''
def print_module_info(args):
    free_ram = gc.mem_free()
    free_rom = _thread.get_heap_size()
    vbat = Power.getVbatt()
    csq = net.csqQueryPoll()
    cdc_log.info('==================================================')
    cdc_log.info('free_ram : {} Bytes'.format(free_ram))
    cdc_log.info('free_rom : {} Bytes'.format(free_rom))
    cdc_log.info('vbat     : {} mV'.format(vbat))
    cdc_log.info('CSQ      : {} '.format(csq))
    cdc_log.info('==================================================')


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

    '''
    此函数循环（间隔30s）打印，用于输出模块信息，便于了解模块运行状态
    如果不需要，请注释下面的定时器调用
    '''
    ostimer.start(30000, 1, print_module_info)

    # 用户代码
    '''######################【User code star】###################################################'''
    count = 0
    while count < 60:
        cdc_log.debug('#### count = {} #####'.format(count))
        count += 1
        utime.sleep(1)
    '''######################【User code end 】###################################################'''

    '''
    只要启用了上面的定时器周期打印系统信息， 在退出main.py之前，必须用下面两行代码来停止和删除定时器；
    用户程序中通过try捕获到异常时，也应该调用下面两行停止与删除定时器；
    如果不需要启用定时器循环打印系统信息，屏蔽上面的 ostimer.start(30000, 1, print_module_info) 时，
    下面两行也需要一起屏蔽！
    '''
    ostimer.stop()
    ostimer.delete_timer()
