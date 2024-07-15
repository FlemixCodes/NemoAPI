from nemo_api.synchrone import NemoAPI


def main():
    # Создаём объект для работы с апи
    nemo_api = NemoAPI("ваш токен")

    # Выполняем метод апи из категории acc (все методы сделан под стиль python acc.getInfo -> acc.get_info)
    response = nemo_api.utils.get_server_time()

    # Также можно выполнять любые методы через request
    response = nemo_api.request("utils.getServerTime")

    # Обращаемся к данным
    print(response['response'])

    # Также можно обращаться к данным через точку
    print(response.response)


if __name__ == "__main__":
    main()
