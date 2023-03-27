from classes import HH, SuperJob


# from vacanсy import HHVacancy, SJVacancy

def check_search(hh: HH, sj: SuperJob) -> bool:
    """Проверка на существование вакансии"""
    return hh.get_request()['items'] != [] or sj.get_request()['objects'] != []
