import socket

def generating_request_with_TCP_payload(ips, port, payload_data, search):
    """
    Генерация запроса c TCP payload
    :param ips: коллекция ip адресов
    :param port: порт
    :param payload_data: донные для payload
    :param search: то что надо найти в ответе
    :return:
    """
    for ip in ips:
        server_address = (f'{ip}', port)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.settimeout(7)
            sock.connect(server_address)
            payload = bytes.fromhex(payload_data)
            sock.sendall(payload)

            response = sock.recv(4096)
            print("Response:", response.hex())
            if search in str(response.hex()):
                print(ip, "Прошёл валидацию")
            else:
                print(ip, "!!! НЕ Прошёл валидацию !!!")
            sock.close()

        except Exception as se:
            print(f"{ip} НЕ Прошёл валидацию! ERROR: {se}")
            sock.close()