import datetime
class Vacancy:


    def __init__(self, name='', url='', description='', salary='', date_published=datetime.datetime.now(), **kwargs):
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary
        self.date_published = date_published


    def __lt__(self, other):
        return self.date_published < other.date_published
    def __str__(self):
        return f'Вакансия - {self.name}, заработная плата - {self.salary} \n;'



class HHVacancy(Vacancy):
    """ HeadHunter Vacancy """

    def __repr__(self):
        return f"HH: {self.name}, зарплата: {self.salary} руб/мес \n;"
    def __str__(self):
        return f'HH: {self.name}, зарплата: {self.salary} руб/мес \n;'
    @property
    def max_salary(self):
        value = self.salary.get('to', 0)
        return 0 if value is None else value
    def __gt__(self, other):
        return self.date_published > other.date_published
    @property
    def datetime(self):
        value = self.date_published
        return value
    #


class SJVacancy(Vacancy):
    """ SuperJob Vacancy """

    def __repr__(self):
        return f"SJ: {self.name}, зарплата: {self.salary} руб/мес \n;"
    def __str__(self):
        return f'SJ: {self.name}, зарплата: {self.salary} руб/мес \n;'

    @property
    def max_salary(self):
        value = self.salary
        return 0 if value is None else value
    def __gt__(self, other):
        return self.date_published > other.date_published
    @property
    def datetime(self):
        value = self.date_published
        return value



# if __name__ == '__main__':
# hh = HHVacancy.datetime
# print(type(hh))
# if len(top_vacancies) == 0:
# return "В вакансиях не указана зарплата"
# else:
# return get_vacancies(top_vacancies)
# def get_top(data, top_count):
# """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """#     pass
