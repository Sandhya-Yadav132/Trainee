import threading
import time

# def task():
#     time.sleep(3)

# t = threading.Thread(target=task)

# print(t.is_alive())

# t.start()

# print(t.is_alive())

# t.join()

# print(t.is_alive())




#-------------------------------------------------------

# What happens if run() calls the target?

# Suppose:

# def task():
#     print(threading.current_thread().name)

# t = threading.Thread(
#     target=task,
#     name="Worker"
# )

# # t.run()   # returns MainThread
# t.start()   # return worker



#----------------------------------------------


def task():
    print(f"Hello {threading.current_thread().name}")
    time.sleep(2)

def dwnld():
    with open("demo.txt",'r') as f:
        data = f.read()
        print(f"Hello {threading.current_thread().name}")
        print(data)

t1 = threading.Thread(target=dwnld, name="Thread1")
t2 = threading.Thread(target=task, name="Thread2")
t3 = threading.Thread(target=task, name="Thread3")


# t1.run()
print(f"Before Execution : {time.time()}")
t1.start()
t1.join()

t2.start()
t2.join()

t3.start()
t3.join()

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

print(f"After Execution : {time.time()}")