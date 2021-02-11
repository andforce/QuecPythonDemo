'''
@Author: Baron
@Date: 2020-06-22
@LastEditTime: 2020-06-22 17:16:20
@Description: example for module _thread
@FilePath: example_thread_file.py
'''
import _thread
import log
import utime
import checkNet


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''
PROJECT_NAME = "QuecPython_Thread_example"
PROJECT_VERSION = "1.0.0"

checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)

# 设置日志输出级别
log.basicConfig(level=log.INFO)
thread_log = log.getLogger("Thread")

a = 0
state = 1
# 创建一个lock的实例
lock = _thread.allocate_lock()

def th_func(delay, id):
	global a
	global state
	while True:
		lock.acquire()  # 获取锁
		if a >= 10:
			thread_log.info('thread %d exit' % id)
			lock.release()  # 释放锁
			state = 0
			break
		a += 1
		thread_log.info('[thread %d] a is %d' % (id, a))
		lock.release()  # 释放锁
		utime.sleep(delay)


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

	for i in range(2):
		_thread.start_new_thread(th_func, (i + 1, i))   # 创建一个线程，当函数无参时传入空的元组

	while state:
		pass