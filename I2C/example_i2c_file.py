import log
from machine import I2C
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_I2C_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

'''
I2C使用示例
'''

# 设置日志输出级别
log.basicConfig(level=log.INFO)
i2c_log = log.getLogger("I2C")


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

    I2C_SLAVE_ADDR = 0x1B  # i2c 设备地址
    WHO_AM_I = bytearray({0x02, 0})   # i2c 寄存器地址，以buff的方式传入，取第一个值，计算一个值的长度

    data = bytearray({0x12, 0})   # 输入对应指令
    i2c_obj = I2C(I2C.I2C0, I2C.STANDARD_MODE)  # 返回i2c对象
    i2c_obj.write(I2C_SLAVE_ADDR, WHO_AM_I, 1, data, 2) # 写入data

    r_data = bytearray(2)  # 创建长度为2的字节数组接收
    i2c_obj.read(I2C_SLAVE_ADDR, WHO_AM_I, 1, r_data, 2, 0)   # read
    i2c_log.info(r_data[0])
    i2c_log.info(r_data[1])

