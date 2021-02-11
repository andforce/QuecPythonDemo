import dataCall
import net
import utime
import checkNet

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_DataCall_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


state = 1
'''
dataCall.setCallback()
用户回调函数，当网络状态发生变化，比如断线、上线时，会通过该回调函数通知用户。
'''
# 定义回调函数
def nw_cb(args):
    global state
    pdp = args[0]   # pdp索引
    nw_sta = args[1]  # 网络连接状态 0未连接， 1已连接
    if nw_sta == 1:
        print("*** network %d connected! ***" % pdp)
    else:
        print("*** network %d not connected! ***" % pdp)
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

    # 注册回调函数
    dataCall.setCallback(nw_cb)

    # 进入飞行模式模拟触发
    net.setModemFun(4)
    utime.sleep(2)

    # 退出飞行模式再次模拟触发回调
    net.setModemFun(1)

    while 1:
        if state:
            pass
        else:
            break
