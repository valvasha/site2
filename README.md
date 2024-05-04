Все актуальные зависимости в requirements.txt
Перед запуском программы, проверьте или установите все зависимости

>> pip install -r requirements.txt

или 

>> python.exe -m pip install -r requirements.txt

Перед запуском приложения проведите все миграции
    Перейдите в папку с проектом джанго (mysite) если вы ещё не в ней.
>> cd mysite

Запустите команду для выполнения всех миграций 
>> python.exe manage.py migrate 

Теперь можно запустить сервер.
>> python.exe manage.py runserver

Доступные url
>> 1. Основной сайт http://127.0.0.1:8000/
>> 2. Работа с ORM (task1) http://127.0.0.1:8000/orm/
>> 3. Информация о студенте (task2) http://127.0.0.1:8000/me/me/

Для корректного отображения страниц на http://127.0.0.1:8000/me/me/

Остановите сервер или откройте новой окно терминала и выполните команду
>> python.exe .\manage.py createsuperuser

Следуйте инструкциям и создайте суперпользователя для управления админ панелью

Перейдите на http://127.0.0.1:8000/admin/ и авторизуйтесь под созданы логином и паролем.

Нам потребуется создать контент для страниц.

1. Откройте в разделе APP_ME Contents
2. Нажмите в правом верхнем углу ADD CONTENT. Вы перейдёте в редактор контента.

Заполните следующие поля
1. Название страницы: равносилен <title></title> Отображается на вкладке
> Может быть произвольным
2. Уникальный url: это отслеживание url страницы http://127.0.0.1:8000/me/<уникальный url>/
> Заполните me без "/" и "."
3. Заголовок в навигации: Отображает название ссылке в меню навигации
> Может быть произвольным, рекомендуется указать такой же как и url
4. Контент: это html код блока content в базовом шаблоне. Воспользуйтесь готовым кодом.
>  Используйте следующий код:
> 
    <section class="about">
        <div class="content">
            <div class="information">
                <h2>Ширяева Валерия Александровна</h2>
                <p>
                    <b>Email:</b> vashiryaeva@edu.hse.ru
                </p>
                <p>
                    <b>Phone:</b> +7(950)442-45-69
                </p>
            </div>
            <div class="photo">
                <img src="/static/app_me/img/me.jpg" alt="me">
            </div>
        </div>
    </section>
    <section class="about">
        <div class="content">
            <div class="information_only">
                <h2>Резюме</h2>
                <p>
                    Основным направлением коммерческой деятельности рассматриваю дизайн и иллюстрации в приложениях
                    экосистемы Adobe, а также фотографию и видео. Являюсь студентом НИУ ВШЭ по направлению менеджмента и
                    на данный момент изучаю углубленные в специализацию бизнес-процессов дисциплины. Помимо учебной
                    деятельности была репетитором по русскому языку индивидуально и в онлайн-школе.
                </p>
            </div>
        </div>
    </section>
5. Порядковый номер в навигации: определяет положение ссылки на страницы по возрастанию.
6. Нажмите SAVE внизу редактора контента

Создайте и заполните ещё три страницы по аналогии. Используйте следующий код для вставки.

Образовательная программа

    <section class="about">
        <div class="content">
            <div class="information_only">
                <h2>Описание моей образовательной программы</h2>
                <a href="https://perm.hse.ru/ba/business/">
                    <h3>ОП “Управление бизнесом”</h3>
                </a>
                <p>
                    Целью образовательной программы «Управление бизнесом» является подготовка современных специалистов с
                    глубокими междисциплинарными знаниями и практическими навыками в области управления бизнесом.
                    Выпускники программы сбалансировано владеют аналитическими, IT и организационными инструментами
                    управления, способны принимать проработанные решения в ключевых сферах деятельности крупных и
                    средних компаний, а также собственных предпринимательских проектах.
                </p>
            </div>
        </div>
    </section>

Менеджемент

    <section class="about">
        <div class="content">
            <div class="information">
                <h2>Руководитель</h2>
                <h3>Артемьев Дмитрий Геннадьевич</h3>
                <p>
                    <b>Email:</b> dartemev@hse.ru
                </p>
            </div>
            <div class="photo">
                <img src="/static/app_me/img/director.jpg" alt="director">
            </div>
        </div>
    </section>

    <section class="about">
        <div class="content">
            <div class="information">
                <h2>Менеджер</h2>
                <h3>Тутынина Ольга Владимировна</h3>
                <p>
                    <b>Email:</b> oshibanova@hse.ru
                </p>
            </div>
            <div class="photo">
                <img src="/static/app_me/img/manager.jpg" alt="manager">
            </div>
        </div>
    </section>

Мои сокурсники

    <section class="about">
        <div class="content">
            <div class="information">
                <h3>Валеев Эмиль Фидаилович</h3>
                <p>
                    <b>Email:</b> efvaleev@edu.hse.ru
                </p>
                <p>
                    <b>Phone:</b> +7(996)123-62-37
                </p>
            </div>
            <div class="photo">
                <img src="/static/app_me/img/student1.jpg" alt="student1">
            </div>
        </div>
    </section>

    <section class="about">
        <div class="content">
            <div class="information">
                <h3>Субботина Полина Андреевна</h3>
                <p>
                    <b>Email:</b> pasubbotina@edu.hse.ru
                </p>
                <p>
                    <b>Phone:</b> +7(919)463-18-88
                </p>
            </div>
            <div class="photo">
                <img src="/static/app_me/img/student2.jpg" alt="student2">
            </div>
        </div>
    </section>