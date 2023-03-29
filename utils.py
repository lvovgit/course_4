from classes import HH, SuperJob
from vacancy import HHVacancy, SJVacancy


# from vacanсy import HHVacancy, SJVacancy

def check_search(hh: HH, sj: SuperJob) -> bool:
    """Проверка на существование вакансии"""
    return hh.get_request()['items'] != [] or sj.get_request()['objects'] != []


def get_only_str_vacancies(data):
    str_vacancies_list = []
    for item in data:
        if item['from'] == 'HeadHunter':
            str_vacancies_list.append(HHVacancy(item))
        else:
            str_vacancies_list.append(SJVacancy(item))
    return str_vacancies_list


def get_top_vacancies_by_salary(data, top_count):
    vacancy_list = []
    for item in data:
        if item['from'] == 'HeadHunter':
            vacancy_list.append(HHVacancy(item))
        else:
            vacancy_list.append(SJVacancy(item))
    # for item in data:
    #     if item.get('salary') is None or data.get('salary').get('from') is None:
    #         continue
    #     else:
    #         vacancy_list.append(item)
    # Сортировка по зарплате
    vacancy_list.sort(key=lambda k: k['salary']['from'], reverse=True)
    top_count_by_salary = vacancy_list[:top_count]
    return top_count_by_salary
