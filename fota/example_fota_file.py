'''
@Author: Pawn
@Date: 2020-07-28
@LastEditTime: 2020-11-30
@Description: example for module fota
@FilePath: example_fota_file.py
'''


import fota
import utime
import log
from misc import Power
import uos
import checkNet

'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Fota_example"
PROJECT_VERSION = "1.0.0"
checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
fota_log = log.getLogger("Fota")

# 此示例需要升级包文件（差分包等.bin文件）

def run():
    fota_obj = fota()  # 创建Fota对象
    file_size = uos.stat("FotaFile.bin")[6]  # 获取文件总字节数
    print(file_size)
    with open("FotaFile.bin", "rb")as f:   # rb模式打开.bin文件(需要制作升级包文件)
        while 1:
            c = f.read(1024)   # read
            if not c:
                break
            fota_obj.write(c, file_size)  # 写入.bin文件数据与文件总字节数

    fota_log.info("flush verify...")
    res = fota_obj.verify()  # 校验
    if res != 0:
        fota_log.error("verify error")
        return
    fota_log.info("flush power_reset...")
    utime.sleep(2)
    Power.powerRestart()   # 重启模块


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

    fota_log.info("run start...")
    run()
