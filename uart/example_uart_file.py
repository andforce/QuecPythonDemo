
"""
运行本例程，需要通过串口线连接开发板的 MAIN 口和PC，在PC上通过串口工具
打开 MAIN 口，并向该端口发送数据，即可看到 PC 发送过来的消息。
"""
import _thread
import utime
import log
from machine import UART
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_UART_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
 * 参数1：端口
        注：EC100YCN平台与EC600SCN平台，UARTn作用如下
        UART0 - DEBUG PORT
        UART1 – BT PORT
        UART2 – MAIN PORT
        UART3 – USB CDC PORT
 * 参数2：波特率
 * 参数3：data bits  （5~8）
 * 参数4：Parity  （0：NONE  1：EVEN  2：ODD）
 * 参数5：stop bits （1~2）
 * 参数6：flow control （0: FC_NONE  1：FC_HW）
'''


# 设置日志输出级别
log.basicConfig(level=log.INFO)
uart_log = log.getLogger("UART")

state = 5


def uartWrite():
    count = 10
    # 配置uart
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    while count:
        write_msg = "Hello count={}".format(count)
        # 发送数据
        uart.write(write_msg)
        uart_log.info("Write msg :{}".format(write_msg))
        utime.sleep(1)
        count -= 1
    uart_log.info("uartWrite end!")


def UartRead():
    global state
    uart = UART(UART.UART2, 115200, 8, 0, 1, 0)
    while 1:
        # 返回是否有可读取的数据长度
        msgLen = uart.any()
        # 当有数据时进行读取
        if msgLen:
            msg = uart.read(msgLen)
            # 初始数据是字节类型（bytes）,将字节类型数据进行编码
            utf8_msg = msg.decode()
            # str
            uart_log.info("UartRead msg: {}".format(utf8_msg))
            state -= 1
            if state == 0:
                break
        else:
            continue



def run():
    # 创建一个线程来监听接收uart消息
    _thread.start_new_thread(UartRead, ())


if __name__ == "__main__":
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

    uartWrite()
    run()
    while 1:
        if state:
            pass
        else:
            break

# 运行结果示例
'''
INFO:UART:Write msg :Hello count=8
INFO:UART:Write msg :Hello count=7
INFO:UART:Write msg :Hello count=6
INFO:UART:Write msg :Hello count=5
INFO:UART:Write msg :Hello count=4
INFO:UART:Write msg :Hello count=3
INFO:UART:Write msg :Hello count=2
INFO:UART:Write msg :Hello count=1
INFO:UART:uartWrite end!
INFO:UART:UartRead msg: read msg 1

INFO:UART:UartRead msg: read msg 2

INFO:UART:UartRead msg: read msg 3
'''
