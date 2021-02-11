import uos
import log
import utime
import checkNet

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Uos_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)


log.basicConfig(level=log.INFO)
uos_log = log.getLogger("Uos")


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

    # 文件操作
    # create a file
    # 创建一个文件操作句柄
    f = open('/usr/test.txt','w')

    # 写入文件
    f.write('hello quecpython!\n')
    f.write('123456789abcdefg!\n')

    # 关闭文件句柄
    f.close()

    # read a file
    f = open('/usr/test.txt', 'r')
    uos_log.info(f.readline())
    uos_log.info(f.readline())
    f.close()

    # 也可使用with方法
    with open('/usr/test.txt','w')as f:
        f.write("hello quecpython!\n")
