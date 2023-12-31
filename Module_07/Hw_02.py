"""
Модифицируем пример предыдущей задачи. Для функции do_setup необходимо 
предусмотреть второй параметр, который будет являться списком зависимостей.

Функция do_setup(args_dict, requires) должна вызывать функцию setup с 
параметрами из словаря args_dict и параметром install_requires, который принимает значение requires.

Структура словаря для параметра args_dicts должна быть следующей

{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}

"""


from setuptools import setup


def do_setup(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires)