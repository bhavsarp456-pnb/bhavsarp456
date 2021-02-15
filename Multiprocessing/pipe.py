from multiprocessing import Process, Pipe
def sender(conn_name, data):
    for msg in data:
        conn_name.send(msg)
        print(f"Sent Message : {msg}")
    conn_name.close()

def receiver(conn_name):
    while True:
        inbox = conn_name.recv()
        if inbox == "END":
            break
        print(f"Received Message : {inbox}")

if __name__ == "__main__":
    msgs = eval(input("Enter the msg:"))
    
    a_con, b_conn = Pipe()
    
    p1 = Process(target=sender, args=(a_con, msgs))
    p2 = Process(target=receiver, args=(b_conn,))

    p1.start()
    p2.start()


    p1.join()
    p2.join()
