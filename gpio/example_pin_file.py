# Pin使用示例

from machine import Pin
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Pin_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
* 参数1：引脚号
        EC100YCN平台引脚对应关系如下：
        GPIO1 – 引脚号22
        GPIO2 – 引脚号23
        GPIO3 – 引脚号38
        GPIO4 – 引脚号53
        GPIO5 – 引脚号54
        GPIO6 – 引脚号104
        GPIO7 – 引脚号105
        GPIO8 – 引脚号106
        GPIO9 – 引脚号107
        GPIO10 – 引脚号178
        GPIO11 – 引脚号195
        GPIO12 – 引脚号196
        GPIO13 – 引脚号197
        GPIO14 – 引脚号198
        GPIO15 – 引脚号199
        GPIO16 – 引脚号203
        GPIO17 – 引脚号204
        GPIO18 – 引脚号214
        GPIO19 – 引脚号215

        EC600SCN平台引脚对应关系如下：
        GPIO1 – 引脚号10
        GPIO2 – 引脚号11
        GPIO3 – 引脚号12
        GPIO4 – 引脚号13
        GPIO5 – 引脚号14
        GPIO6 – 引脚号15
        GPIO7 – 引脚号16
        GPIO8 – 引脚号39
        GPIO9 – 引脚号40
        GPIO10 – 引脚号48
        GPIO11 – 引脚号58
        GPIO12 – 引脚号59
        GPIO13 – 引脚号60
        GPIO14 – 引脚号61
* 参数2：direction
        IN – 输入模式
        OUT – 输出模式
* 参数3：pull
        PULL_DISABLE – 禁用模式
        PULL_PU – 上拉模式
        PULL_PD – 下拉模式
* 参数4：level
        0 设置引脚为低电平
        1 设置引脚为高电平
'''
gpio1 = Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0)

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

    gpio1.write(1) # 设置 gpio1 输出高电平
    val = gpio1.read() # 获取 gpio1 的当前高低状态
    print('val = {}'.format(val))
