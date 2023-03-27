import os
from classes import Engine, HH, SuperJob
from utils import check_search

def main():
    path = os.path.join('../course_4_parser/filename.json')
    connector = Engine.get_connector(path)

    search_keyword = input('Введите ключевое слово поиска')

    hh = HH(search_keyword)
    sj = SuperJob(search_keyword)
    if check_search(hh, sj):
        all = hh.get_vacancies + sj.get_vacancies
        connector.insert(all)

    else:
        print('Такой вакансии нет')

    top_count = input('Укажите какое количество вакансий будем выводить на экран\n')
    if not top_count.isdigit() or int(top_count) <= 0:
        print('Количество должно быть целым числом больше ноля. Попробуйте еще раз')

    else:
        top_count = int(top_count)
    #


if __name__ == '__main__':
    main()