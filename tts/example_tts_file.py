'''
@Author: Pawn
@Date: 2020-08-19
@Description: example for module TTS
@FilePath: example_tts_file.py
'''
import log
from audio import TTS
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_TTS_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
tts_Log = log.getLogger("TTS")


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

    # 参数1：device （0：听筒，1：耳机，2：喇叭）
    tts = TTS(1)
    # 获取当前播放音量大小
    volume_num = tts.getVolume()
    tts_Log.info("Current TTS volume is %d" %volume_num)

    # 设置音量为6
    volume_num = 6
    tts.setVolume(volume_num)
    #  参数1：优先级 (0-4)
    #  参数2：打断模式，0表示不允许被打断，1表示允许被打断
    #  参数3：模式 （1：UNICODE16(Size end conversion)  2：UTF-8  3：UNICODE16(Don't convert)）
    #  参数4：数据字符串 （待播放字符串）
    tts.play(1, 1, 2, 'QuecPython') # 执行播放
    tts.close()   # 关闭TTS功能