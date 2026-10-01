# # import threading
# # import time


# # def func(args, delay):
# #     print(args * args)
# #     time.sleep(delay)

# # t1 = threading.Thread(target = func, args = (4, 2))
# # t2 = threading.Thread(target = func, args = (5, 2))

# # t1.start()
# # t2.start()

# # # t1.join()
# # # t2.join()

# # print("Done")



# import threading
# import time

# def download_file(file_name, delay):
#     print(f"Starting reading: {file_name}")
#     with open(file_name, 'r') as f:
#         data = f.read()
#     time.sleep(delay)  # Simulates a network delay (I/O bound)
#     print(f"Finished reading: {file_name}:\n{data}")

# # 1. Create thread objects
# thread1 = threading.Thread(target=download_file, args=("demo.txt", 2))
# thread2 = threading.Thread(target=download_file, args=(r"filehandling\demo.txt", 2))

# # 2. Start execution
# thread1.start()
# thread2.start()

# # 3. Wait for threads to complete before moving the main script forward
# thread1.join()
# thread2.join()

# print("All downloads complete!")


import threading
import time


def func(n, s):
    print(f"Thread {n}")
    time.sleep(s)

t1 = threading.Thread(target = func, args = (1, 2))
t2 = threading.Thread(target = func, args = (2, 2))
t3 = threading.Thread(target = func, args = (3, 2))

t1.start()
t2.start()

t3.run()

# t1.join()
# t2.join()

# t1.run()

# t1.join()

# t1.start()    #RuntimeError: threads can only be started once
print("Done")
