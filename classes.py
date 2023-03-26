import json
from abc import abstractmethod, ABC

import requests

from connector import Connector


class Engine(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_request(self):
        """Абстрактный метод запросов"""
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        return Connector(file_name)


class HH(Engine):
    """Класс с методами для HeadHunter"""
    URL = 'https://api.hh.ru/vacancies/'

    def __init__(self, search_keyword):
        super().__init__()
        self.params = None

    def get_request(self):
        """Запрос вакансий API HeadHunter"""
        self.params = {
            'text': f'{search_keyword}',
            'per_page': 100,
            'area': 113,
            'page': 0


        }
        response = requests.get(self.URL, params=self.params)
        data = response.content.decode()
        response.close()

        js_hh = json.loads(data)
        print(js_hh)
        return js_hh

    # def to_json(self, value):
    #     with open("../course_4_parser/filename.json", "w", encoding="UTF-8") as file:
    #         print(json.dump(value, file, indent=2, ensure_ascii=False))
    # @staticmethod
    def get_info_vacancy(self, data):

        info = {
            'name': data.get('name'),
            'url': data.get('alternate_url'),
            'description': data.get('snippet').get('responsibility'),
            'salary': data.get('salary'),
            'date_published': data.get('published_at'),
            'experience': data.get('experience'),
            'page_number': data.get('page')
        }
        return info

    @property
    def get_vacancies(self):
        """Записывает информацию о вакансии в список при наличии сведений о ЗП в рублях"""
        vacancies = []
        data = self.get_request()
        while len(vacancies) <= 500:
            for vacancy in data.get('items'):
                if vacancy.get('salary') is not None and vacancy.get('salary').get('currency') == 'RUR':
                    vacancies.append(self.get_info_vacancy(vacancy))
                    self.params['page'] += 1
                else:
                    break
        print(len(vacancies))
            # if data.get('found') <= 500 and self.params['page'] == 0:
        return vacancies


# class SuperJob(Engine):
#     URL = 'https://api.superjob.ru/2.0/vacancies/'
#
#     def __init__(self):
#         super().__init__()
#
#     def get_request(self):
#         headers = {
#             'Host': 'api.superjob.ru',
#             'X-Api-App-Id': os.getenv('SJ_API_KEY'),
#             'Authorization': 'Bearer r.000000010000001.example.access_token',
#             'Content-Type': 'application/x-www-form-urlencoded'
#         }
#         params = {'keyword': 'Python', 'count': 100,  'page': 1}
#         response = requests.get(self.URL, headers=headers, params=params)  # .json()
#
#         data = response.content.decode()
#         response.close()
#         js_sj = json.loads(data)
#         return js_sj
#
#     def to_json(self, value):
#         with open("../course_4_parser/filename.json", "w", encoding="UTF-8") as file:
#             print(json.dump(value, file, indent=2, ensure_ascii=False))
#
#     @staticmethod
#     def get_info_vacancy(data):
#         info = {
#             'name': data['objects'][0]['profession'],
#             # 'url': data['items'][0]['alternate_url'],
#             # 'description': data['items'][0]['snippet']['responsibility'],
#             # 'salary': data.get('salary'),
#             # 'date_published': data['items'][0]['published_at']
#         }
#         return info


if __name__ == '__main__':
    search_keyword = 'Python'
    hh = HH(search_keyword)
    # k = hh.get_request()
    #
    # i = hh.get_info_vacancy(k)
    # #print(i)
    i = hh.get_vacancies
    df = Connector('../course_4_parser/filename.json')
    # df.connect
    df.insert(i)

    # sj = SuperJob()
    # k = sj.get_request()
    # sj.to_json(k)
    # print(sj.get_info_vacancy(k))
