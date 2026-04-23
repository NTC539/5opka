"""
This script runs the application using a development server.
"""
import cProfile
import pstats

import bottle
import os
import sys

# routes contains the HTTP handlers for our server and must be imported.
import routes
import myform

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return bottle.default_app()


if __name__ == '__main__':
    # Настройка параметров сервера
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = 5555

    # Создаем объект профилировщика
    profiler = cProfile.Profile()
    profiler.enable()

    try:
        # Запускаем сервер
        bottle.run(server='wsgiref', host=HOST, port=PORT)
    finally:
        profiler.disable()
        # Вывод статистики после остановки сервера
        stats = pstats.Stats(profiler).sort_stats('cumtime')
        stats.print_stats(20)  # Вывести топ-20 самых «тяжелых» функций
