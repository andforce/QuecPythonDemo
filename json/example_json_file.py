'''
@Author: Baron
@Date: 2020-06-17
@LastEditTime: 2020-06-17 17:06:08
@Description: example for module ujson
@FilePath: example_json_file.py
'''

# ujson.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

import ujson
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Json_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
ujson_log = log.getLogger("UJSON loads")


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

    inp = {'bar': ('baz', None, 1, 2)}
    ujson_log.info(type(inp))
    # <class 'dict'>

    # 将Dict转换为json
    s = ujson.dumps(inp)
    ujson_log.info(s)
    ujson_log.info(type(s))
    # {"bar": ["baz", null, 1, 2]}, <class 'str'>

    # 将json转换为Dict
    outp = ujson.loads(s)
    ujson_log.info(outp)
    ujson_log.info(type(outp))
    # ujson.dump()和juson.load()主要用来读写json文件
