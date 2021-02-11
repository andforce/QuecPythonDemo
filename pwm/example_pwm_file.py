# PWM使用示例

from misc import PWM
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_PWM_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
* 参数1：PWM号
        注：EC100YCN平台，支持PWM0~PWM3，对应引脚如下：
        PWM0 – 引脚号19
        PWM1 – 引脚号18
        PWM2 – 引脚号23
        PWM3 – 引脚号22

        注：EC600SCN平台，支持PWM0~PWM3，对应引脚如下：
        PWM0 – 引脚号52
        PWM1 – 引脚号53
        PWM2 – 引脚号70
        PWM3 – 引脚号69
* 参数2：high_time
        高电平时间，单位ms
* 参数3：cycle_time
        pwm整个周期时间，单位ms
'''
# 需要配合外设或者使用杜邦线短接对应引脚测试

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

    pwm = PWM(PWM.PWM0, PWM.ABOVE_MS, 100, 200)  # 初始化一个pwm对象
    pwm.open()  # 开启PWM输出
    utime.sleep(10)
    pwm.close()  # 关闭pwm输出