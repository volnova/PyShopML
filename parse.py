# -*- coding: utf-8 -*-
"""Разработайте скрипт на Python, который будет выводить в консоль (STDOUT) информацию
 о предстоящих событиях анонсированных на главной странице python.org (Upcoming Events).
 Вывод информации оформите по своему усмотрению. Выбор библиотек на ваше усмотрение."""

import requests
from lxml import html


def request_to_site():
    r = requests.get('https://www.python.org/')
    root = html.fromstring(r.text)
    event_list = root.xpath('.//div[@class="medium-widget event-widget last"]/div/ul')
    events = event_list[0].xpath('.//li/a/text()')
    dates = event_list[0].xpath('.//li/time/@datetime')
    for i in xrange(len(events)):
        print dates[i][:10], events[i]


request_to_site()
