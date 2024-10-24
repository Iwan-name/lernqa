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

def get_xapk_using_proxy(URLS, file_name: str) -> None:
    """
    Функция для скачивания XAPK файла.
    :param file_name: Имя приложения
    :return: None
    """
    for url in URLS:
        logging.info(f"Попытка скачать XAPK c URL: {url}")
        result = self._request_via_proxy(method="get", url=url) # запрс с прксями
        if result.status_code == 200:
            with open(file_name, "wb") as file:
                for chunk in result.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                logging.info("Файл XAPK скачен")
                break
        else:
            logging.info(f"Не получилось скачать XAPK c URL: {url} ")
    else:
        messages = "Файл XAPK не удалось скачать. Работа сборщика остановлена"
        logging.error(messages)
        raise Exception(messages)
