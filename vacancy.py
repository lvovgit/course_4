class Vacancy:
    __slots__ = ('name', 'url', 'description', 'salary', 'date_published')

    def __init__(self, data: dict):
        self.name = data.get('name')
        self.url = data['url']
        self.description = data['description']
        self.salary = data.get('salary')
        self.date_published = data['date_published']

    def __str__(self):
        return f'Вакансия - {self.name}, заработная плата - {self.salary} \n;'


# class ClassMixin:




class HHVacancy(Vacancy):
    """ HeadHunter Vacancy """

    def __repr__(self):
        return f"HH: {self.name}, зарплата: {self.salary} руб/мес \n;"
    def __str__(self):
        return f'HH: {self.name}, зарплата: {self.salary} руб/мес \n;'


class SJVacancy(Vacancy):
    """ SuperJob Vacancy """

    def __repr__(self):
        return f"SJ: {self.name}, зарплата: {self.salary} руб/мес \n;"
    def __str__(self):
        return f'SJ: {self.name}, зарплата: {self.salary} руб/мес \n;'


# def sorting(vacancies):
#     """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
#     pass
#




    # if len(top_vacancies) == 0:
    #     return "В вакансиях не указана зарплата"
    # else:
    #     return get_vacancies(top_vacancies)

# def get_top(data, top_count):
#     """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """#     pass
