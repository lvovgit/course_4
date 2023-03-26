import os

from classes import Engine, HH, SuperJob

def main():
    path = os.path.join('../course_4_parser/filename.json')
    connector = Engine.get_connector(path)

    search_keyword = input('Введите ключевое слово поиска')

