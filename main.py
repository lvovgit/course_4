import os
from classes import Engine, HH, SuperJob
from utils import check_search, get_top_vacancies_by_salary, get_only_str_vacancies
from vacancy import HHVacancy, SJVacancy


def main():
    global all_vacancies, k
    path = os.path.join('../course_4_parser/filename.json')
    path2 = os.path.join('../course_4_parser/all')  # задаем путь до файла с вакансиями
    connector = Engine.get_connector(path)  # создаем экземпляр класса Connector функцией get_connector из класса Engine

    search_keyword = input('Введите ключевое слово поиска')

    hh = HH(search_keyword)
    sj = SuperJob(search_keyword)
    if check_search(hh, sj):
        all_vacancies = hh.get_vacancies + sj.get_vacancies
        connector.insert(path, all_vacancies)


    else:
        print('Такой вакансии нет')

    top_count = input('Колличество выводимых на экран вакансий')
    if not top_count.isdigit() or int(top_count) <= 0:
        print('Необходимо ввести целое число ')

    else:
        top_count = int(top_count)

    all_vacancies = connector.select({})
    vacancies = get_only_str_vacancies(all_vacancies)
    # print(" ".join(str(x) for x in vacancies))
    # with open(path2, 'a', encoding="UTF-8") as file:
    #     file.write("\n".join(str(x) for x in vacancies))
    # with open(path2, 'w', encoding="UTF-8") as file:
    #     x = file.read().split()
    # vacancies.sort(key=lambda x: x['salary'])
    #print(vacancies)

    # print(vacancies)
    print(type(vacancies))
    # with open('../course_4_parser/vacancies.txt', 'w', encoding='windows-1251') as file:
    #     file.write({vacancies})

    top_1 = get_top_vacancies_by_salary(vacancies, top_count)
    print(top_1)


if __name__ == '__main__':
    main()
