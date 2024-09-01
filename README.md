# **Geogramint_custom - OSINT инструмент для поиска пользоваталей и групп по геолокации в Telegram**

<p align="center">
<img src="https://github.com/Alb-310/Geogramint/blob/master/appfiles/Geogramint.png" width="300"/>
</p>

<p align="center"> <img src="https://img.shields.io/badge/version-1.4-orange" /> <img src="https://img.shields.io/badge/PYTHON-03b1fc?style=for-the-badge&logo=python"/> <a href="https://github.com/Alb-310"> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/><a/> <a href="https://twitter.com/Alb_310"> <img src="https://github.com/Alb-310/Geogramint/blob/master/.github/by-alb310.svg"/><a/> <img src="https://img.shields.io/badge/License-GPLv3-blue.svg"/>
<p align="center"> <a href="https://projetfox.com/"> <img src="https://github.com/Alb-310/Geogramint/blob/master/.github/fox%20badge.png" width="200"/> <a/>

## **Описание**

Geogramint_custom - приложение для поиска пользователей и групп, используя API телеграм с подключенной БД MongoDB, но без графического интерфейса.

### Оригинальное приложение доступно по ссылке: [Geogramint](https://github.com/Alb-310/Geogramint/)<br>

## 🛠️ Установка

**Требования:** [Python 3.9, 3.10 or 3.11](https://www.python.org/downloads/release/python-3112/)<br>

### Windows [![Windows](https://img.shields.io/badge/Windows-03b1fc?style=for-the-badge&logo=windows)](https://svgshare.com/i/ZhY.svg)

+ #### Github

```bash
git clone https://github.com/Alimovriq/Geogramint_custom.git
cd Geogramint_custom/
py -m venv env
py env/Scripts/activate
py -m pip install --upgrade pip
pip3 install -r requirements.txt
```

- [Установить актуальную версию клиента MongoDB](https://www.mongodb.com/try/download/community);
- Создать файл в корне проекта Geogramint_custom/.env и указать параметры как в файле Geogramint_custom/.env_example;
- Открыть приложение MongoDB.

```bash
py geogramint.py --help # для CLI режима
```

### Mac OS  ![macOS](https://img.shields.io/badge/Mac_OS-abbfc7?style=for-the-badge&logo=apple) и Linux ![Linux](https://img.shields.io/badge/Linux-ffffff?style=for-the-badge&logo=linux)

+ #### Github

```bash
git clone https://github.com/Alimovriq/Geogramint_custom.git
cd Geogramint_custom/
python/python3 -m venv env
source env/bin/activate
python/python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

python3 geogramint.py --help # для CLI режима
```

### Все ОС
1. [Установить актуальную версию клиента MongoDB](https://www.mongodb.com/try/download/community)
2. Создать файл в корне проекта Geogramint_custom/.env и указать параметры как в файле Geogramint_custom/.env_example
3. 

## 📡 Пример: CLI (терминал)

1. Создать API key для Вашего Telegram аккаунта [здесь](https://my.telegram.org). Необходимо установить изображение пользователя в настройке `Приватность и безопасность`, разрешить другим пользователям видеть изображение Вашего профиля.

<p align="center"> <img src="https://github.com/Alb-310/Geogramint/blob/master/.github/privacy_settings.jpg" width="300"/>

2. Запуск **Geogramint_custom**

![image](https://user-images.githubusercontent.com/52386954/210659094-506e3018-6784-4602-bf4e-e446534f6f15.png)

3. Комманда для установки базовых значений `set-config`, укажите параметры (api_id, api_hash and phone number)

![image](https://user-images.githubusercontent.com/52386954/210659472-dbb1804e-dd8a-468e-b0a1-bfcd77652113.png)

4. Комманда для поиска `start-scan` с двумя аргументами (ширина и долгота) `lat lon`:

![image](https://user-images.githubusercontent.com/52386954/210659762-4fffc2ac-957d-4377-9615-d339dcb17aef.png)

 <p align="center"> <img src="https://user-images.githubusercontent.com/52386954/210661716-9a3db8c7-4627-447e-b18b-dcf2c8c54a36.png" width="500"/>
  <p align="center"> ⬇ </p>
  
<p align="center"> <img src="https://user-images.githubusercontent.com/52386954/210661742-7e7a6242-5915-4b0e-a52d-38d4dd779eff.png" width="500"/>

5. Вывод результатов:

+ зеленый в радиусе 500м
+ желтый в радиусе 1000м
+ оранжевый в радиусе 2000м
+ красный в радиусе >3000м

(Примечание: Результаты могут быть экспортированы в завимисоти от опций комманды `start-scan`. По умолчанию изображения пользователей и остальные данные сохраняются в `json` и находятся в `Geogramint_custom/cache_telegram/`)

6. `reset-scan` очистит `cache_telegram` и все объекты базы данных.
  
## 📝 Лицензия

[MIT license](https://opensource.org/license/mit)
