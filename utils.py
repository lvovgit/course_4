import json

from classes import HH, SuperJob
from vacancy import HHVacancy, SJVacancy


# from vacanсy import HHVacancy, SJVacancy

def check_search(hh: HH, sj: SuperJob) -> bool:
    """Проверка на существование вакансии"""
    return hh.get_request()['items'] != [] or sj.get_request()['objects'] != []


def get_only_str_vacancies(data):
    str_vacancies_list = []
    hh = HHVacancy
    sj = SJVacancy
    for item in data:
        if item['from'] == 'HeadHunter':
            str_vacancies_list.append(hh(item))
        else:
            str_vacancies_list.append(sj(item))
    return str_vacancies_list


def get_top_vacancies_by_salary(data, top_count):
    sorted(data, key=lambda i: i['salary'])
    top_count_by_salary = vacancy_list_by_salary[:top_count]
    #vacancy_list_by_salary = []
    #for item in data:
        # if item["salary"] is None:
        #     item["salary"] = {}
        #     item["salary"]["from"] = 0
        #     item["salary"]["to"] = 0
        #     vacancy_list_by_salary.append(item)

       #else:
        #    continue
        #vacancy_list_by_salary.sort(key=lambda i: i["salary"])
        #top_count_by_salary = vacancy_list_by_salary[:top_count]
        #return top_count_by_salary
  # if item["salary"] is None:
        #     item["salary"] = {}
        #     item["salary"]["from"] = 0
        #     item["salary"]["to"] = 0
        #     vacancy_list_by_salary.append(item)