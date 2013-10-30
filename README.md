# pySMSPilot

## English

### Description

Python class with Implementation for SMS sending gateway API <http://www.smspilot.ru/>
You need regisration and API-Key to start using it. We use some features from API 2.3.2.
API provider gives some free sms for testing purposes, henceforward you need to pay some
fee for them. Prices provided on their site.
Now available at PyPI. You can install it by running: pip install pySMSPilot

### Installation ang quick start

After registering at <http://www.smspilot.ru/>:
1. Include it with:

import smspilot

2. Initilize class with your API-key:

Pilot = smspilot.Sender(api)

3. Add some sms messages with command:

Pilot.addSMS([your_local_sms_id_int], "Phone number", u"SMS message", u"Sender name")

**Note:** phone number must be in format 7xxxxxxxxxx

**Note:** sender name must contain only latin letters dots and dashes, min length 3 letters, max - 11

**Note:** Ability to change sender name may be limited by service rules, refer to http://www.smspilot.ru/ to find out more

4. Run sending command with:

Result = Pilot.send()

Object with sending results will be returned. More info look at <http://www.smspilot.ru/apikey.php>


## Russian

### Описание

Класс имлементации использования API (версии 2.x) сайта http://www.smspilot.ru/ для отправки SMS рассылок.
Для отправки смс необходима регистрация на сайте. Провайдер предоставляет несколько бесплатных смс для тестирования. Но в дальнейшем нужно оплачивать отправку каждого смс. Прайсы на сайте. По России недорого. Ок. 30 копеек за смс на сегодня.
Теперь библиотека доступна через PyPI. Для установки просто выполните: pip install pySMSPilot

### Инструкции

1. Подключить модуль:

import smspilot

2. Инициализировать класс API-ключом:

Pilot = smspilot.Sender(api)

3. Добавим одно или несколько sms вот так:

Pilot.addSMS([локальный_id_сообщения_int],"Номер телефона", u"SMS сообщение", u"Imya Otpravitelya")

**Note:** номер телефона должен быть в формате 7xxxxxxxxxx

**Note:** Imya Otpravitelya - имя отправителя может содежать только латинские буквы, точки и тире, длинна мин 3 символа, макс - 11

**Note:** возможность изменять имя отправителя может быть ограничена сервисом, подробнее см. условия на сайте http://www.smspilot.ru/

4. Запускаем комманду отправки:

Result = Pilot.send()

Будет возвращен объект с результатами отправки. Больше информации см. <http://www.smspilot.ru/apikey.php>

Copyright (c) 2013 by Stanislav Sokolov aka Ratso
