'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module urandom
@FilePath: example_urandom_file.py
'''
import urandom as random
import log
import utime
import checkNet

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Random_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

log.basicConfig(level=log.INFO)
random_log = log.getLogger("random")


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

    # urandom.randint(start, end)
    # 随机1 ~ 4之间
    num = random.randint(1, 4)
    random_log.info(num)

    # random between 0~1
    num = random.random()
    random_log.info(num)

    # urandom.unifrom(start, end)
    # 在开始和结束之间生成浮点数
    num = random.uniform(2, 4)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # 2-bit binary,the range is [00~11] (0~3)
    num = random.getrandbits(2)
    random_log.info(num)

    # 8-bit binary,the range is [0000 0000~1111 11111] (0~255)
    num = random.getrandbits(8)
    random_log.info(num)

    # urandom.randrange(start, end, step)
    # 从开始到结束随机生成递增的正整数
    num = random.randrange(2, 8, 2)
    random_log.info(num)

    # urandom.choice(obj)
    # 随机生成对象中元素的数量
    num = random.choice("QuecPython")
    random_log.info(num)
