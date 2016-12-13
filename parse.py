# -*- coding: utf-8 -*-
"""Разработайте скрипт на Python, который будет выводить в консоль (STDOUT) информацию
 о предстоящих событиях анонсированных на главной странице python.org (Upcoming Events).
 Вывод информации оформите по своему усмотрению. Выбор библиотек на ваше усмотрение."""

import requests
from lxml import html


def request_to_site():
    try:
        request = requests.get('https://www.python.org/')
        root = html.fromstring(request.text)
        event_list = root.xpath('.//div[@class="medium-widget event-widget last"]')
        events = event_list[0].xpath('.//li/a/text()')
        dates = event_list[0].xpath('.//li/time/@datetime')
        for i in xrange(len(events)):
            print dates[i][:10], events[i]
    except requests.exceptions.ConnectionError:
        print "No connection to site"
    except IndexError:
        print "There are no Upcoming Events"

if __name__ == '__main__':
    request_to_site()
