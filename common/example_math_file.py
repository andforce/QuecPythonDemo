# 数学运算math函数示例

import math
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Math_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


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

    # 设置日志输出级别
    log.basicConfig(level=log.INFO)
    math_log = log.getLogger("Math")

    # x**y运算后的值
    result = math.pow(2,3)
    math_log.info(result)
    # 8.0

    # 取大于等于x的最小的整数值，如果x是一个整数，则返回x
    result = math.ceil(4.12)
    math_log.info(result)
    # 5

    # 把y的正负号加到x前面，可以使用0
    result = math.copysign(2,-3)
    math_log.info(result)
    # -2.0

    # 求x的余弦，x必须是弧度
    result = math.cos(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # 把x从弧度转换成角度
    result = math.degrees(math.pi/4)
    math_log.info(result)
    # 45.0

    # e表示一个常量
    result = math.e
    math_log.info(result)
    # 2.718281828459045

    # exp()返回math.e(其值为2.71828)的x次方
    result = math.exp(2)
    math_log.info(result)
    # 7.38905609893065

    # fabs()返回x的绝对值
    result = math.fabs(-0.03)
    math_log.info(result)
    # 0.03

    # floor()取小于等于x的最大的整数值，如果x是一个整数，则返回自身
    result = math.floor(4.999)
    math_log.info(result)
    # 4

    # fmod()得到x/y的余数，其值是一个浮点数
    result = math.fmod(20,3)
    math_log.info(result)
    # 2.0

    # frexp()返回一个元组(m,e),其计算方式为：x分别除0.5和1,得到一个值的范围，2e的值在这个范围内，e取符合要求的最大整数值,然后x/(2e),得到m的值。如果x等于0,则m和e的值都为0,m的绝对值的范围为(0.5,1)之间，不包括0.5和1
    result = math.frexp(75)
    math_log.info(result)
    # (0.5859375, 7)

    # isfinite()如果x不是无穷大的数字,则返回True,否则返回False
    result = math.isfinite(0.1)
    math_log.info(result)
    # True

    # isinf()如果x是正无穷大或负无穷大，则返回True,否则返回False
    result = math.isinf(234)
    math_log.info(result)
    # False

    # isnan()如果x不是数字True,否则返回False
    result = math.isnan(23)
    math_log.info(result)
    # False

    # ldexp()返回x*(2**i)的值
    result = math.ldexp(5,5)
    math_log.info(result)
    # 160.0

    # modf()返回由x的小数部分和整数部分组成的元组
    result = math.modf(math.pi)
    math_log.info(result)
    # (0.14159265358979312, 3.0)

    # pi:数字常量，圆周率
    result = math.pi
    math_log.info(result)
    # 3.141592653589793

    # sin()求x(x为弧度)的正弦值
    result = math.sin(math.pi/4)
    math_log.info(result)
    # 0.7071067811865476

    # sqrt()求x的平方根
    result = math.sqrt(100)
    math_log.info(result)
    # 10.0

    # tan()返回x(x为弧度)的正切值
    result = math.tan(math.pi/4)
    math_log.info(result)
    # 0.9999999999999999

    # trunc()返回x的整数部分
    result = math.trunc(6.789)
    math_log.info(result)
    # 6
