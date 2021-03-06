"""
    udp多线程聊天小程序
    主线程：接收键盘输入
    线程1：收数据
    线程2：发数据
"""
import socket, threading

def send_msg(udp_socket):
    data = input("请输入你想要说的话:")
    ip_address = input("请输入目的地的ip地址:")
    port = int(input("请输入目的地的端口号:"))
    udp_socket.sendto(data.encode(encoding="utf-8"), (ip_address, port))


def recv_msg(udp_socket):
    # 线程内循环接收数据
    while True:
        recv_data, remote_address = udp_socket.recvfrom(1024)
        print("收到来自: %s 的数据：%s" % (str(remote_address), recv_data.decode(encoding="utf-8")))

def main():
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 8888))
    # 创建线程收数据
    recv_thd = threading.Thread(target=recv_msg, args=(udp_socket,))
    recv_thd.start()

    while True:
        op = input("请输入需要进行的操作: 1 发送数据 2 接收数据 3 退出")
        if op == "1":
            send_msg(udp_socket)
        # elif op == "2":
        #     recv_msg(udp_socket)
        elif op == "3":
            break
        else:
            print("你的输入有错,请重新输入...")

    # 关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()