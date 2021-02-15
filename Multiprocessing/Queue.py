from multiprocessing import Queue

L = Queue(maxsize = 6)
print(L.qsize())

L.put(9)
L.put(8)
L.put(5)
L.put(4)
L.put(2)
L.put(3)

print("Full:", L.full())
print("Size:",L.qsize())

L.get()
L.get()
L.get()
L.get()
L.get()
L.get()

print("Empty:",L.empty())
