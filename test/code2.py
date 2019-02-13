from threading import Thread
import time

class Email(Thread):

    def testa(self, b):
        print('test'+str(b))
        t.start()

    def run(self):
        print('等待')
        time.sleep(5)
        # self.testa('bb')

print('主线程')
for i in range(5):
    t = Email()
    t.testa(f'{t.getName()}=={i}')
# t.join()
print('主线程会继续嘛')
