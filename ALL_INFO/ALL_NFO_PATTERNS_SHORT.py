"""

 Самое Важное!!!
 Всегда ДУМАТЬ! перед тем, как что-либо сделать, необходимо всё тщательно обдумать

 Радоваться Жизни  Радоваться разным мелочам

 Ценить:         Ценить то что есть и стремиться к лучшему, Ценить сегодняшний день и брать МАКСИМУМ
 Быть проще:     Ко всему относиться Проще и Спокойнее без Волнения
 Слушать Других: Прислушиваться к мнению других людей они могут быть правы  И делать выводы
 Время:          Тайм-менеджмент   Грамотное распределение времени, Контроль Времени, Правильно раставлять Приоритеты
 Уверенность:    Быть уверенным в себе НО Оценивать свои силы!
 Развития:       Развиваться, Учиться, учиться и ещё раз - учиться, Саморазвитие
 Не Надеяться:   Надеяться только на себя
 Контроль:       Быть менее Эмоциональным, Совладать с Эмоциями, Контролировать свои эмоции в любой ситуации
 Внимательность: Быть Внимательным
 Спокойствие:    Быть Спокойнее, Перестать Нервничать , Быть Расслабленным, Не Злиться на себя и на других
 Режим:          Правильный Сон, Пить Воду
 Зарядка:        Бег, Тренировки, Стойка на Голове
 Тельце в тепле: НЕ переохлаждаться

 Молчание золото:  Лучше промолчать, чем сказать и потом жалеть о том, что сказал
 Соломон:          Все пройдёт, и это тоже пройдёт
 Вообще это замечательный подход: осознать, что проблема не такая уж и проблема, и вполне решаема.
 Кто ищет-тот всегда найдет!
 Искать Другие способы
 Не спеши, а то успеешь...   Успеешь, но не туда куда хотел...
 Подумай, нужно ли тебе ЭТО и для Чего
 Надо принимать вещи такими, как они есть, и пользоваться ими с наибольшей для себя выгодой.
 Если научиться принимать вещи как они есть, страдание исчезнет.
________________________________________________________________________________________________________________________

 Книга о разработке и алгоритмах. Банда Четырех Паттерны Проектирования.
 Авторы: Гамма Эрих, Хелм Ричард, Джонсон Роберт, Влиссидес Джон

Порождающие паттерны:

 1)  Абстрактная фабрика (Abstract factory):
 создает семейства связанных объектов, не привязываясь к конкретным классам создаваемых объектов.


 2)  Строитель (Builder):
 От абстрактной фабрики отличается тем, что делает акцент на пошаговом конструировании объекта.
 Строитель возвращает объект на последнем шаге, тогда как абстрактная фабрика возвращает объект немедленно.

 Используется для пошагового создания сложных обьектов


 3)  Фабричный метод (Factory method):
 Создает объекты без указания точного класса, но оставляет подклассам решение о том, какой класс инстанцировать.

 Инстанцирование — создание экземпляра класса

 4) Прототип (Prototype):
 Создает новые экземпляры объекта путем клонирования прототипа: Пример Модуль copy


 5) Одиночка (Singleton):
 У класса есть только один экземпляр : Пример Модуль — это файл с расширением .py

 С помощью паттерна одиночка могут быть реализованы многие паттерны (АБСТРАКТНАЯ ФАБРИКА, СТРОИТЕЛЬ, ПРОТОТИП).


Структурные паттерны:

 1) Адаптер (Adapter):
  позволяет объектам с несовместимыми интерфейсами работать вместе


 2) Мост (Bridge):
  Отделяет абстракцию от ее реализации так, чтобы и то и другое можно было изменять независимо.


 3) Компоновщик (Composite):
  упрощает создание иерархий объектов:  Python это не особенно нужно, так как для этой цели хватает словарей

  Описывает группу объектов, которая рассматривается как один экземпляр.


 4) Декоратор (Decorator):
 Динамически Добавляет дополнительную функциональность, не изменяя класс.


 5) Фасад (Facade):
 Фасад надстраивает простой интерфейс поверх сложного

  Фасад надстраивает простой интерфейс поверх сложного,
  Адаптер надстраивает унифицированный интерфейс над каким-то другим (необязательно сложным).

 Унифицировать - приведение к единообразию, к единому виду
 Унифицированный интерфейс упрощает поддержку версионности(способность иметь версии), что облегчает последующую эволюцию продукта.

 6) Приспособленец (Flyweight):
 для уменьшения затрат памяти при работе с большим количеством мелких объектов:  Пример - Менеджер памяти Python


 7) Заместитель (Proxy, Surrogate)
 позволяет создать объект-замену для другого объекта: Пример - Mock(макет-пустышка)


 Поведенческие Паттерны :

 1) Цепочка ответственности (Chain of responsobility):
  Цель Разрешить передачу запроса по цепочке получателей до тех пор, пока он(запрос) не будет обработан.


 2) Команда (Command):
  превращает запросы в объекты, позволяя передавать их как аргументы при вызове методов, Пример: Django HttpRequest (без метода выполнения)
  ставить запросы в очередь, логировать их, а также поддерживать отмену операций


 3) Интерпретатор (Interpreter):
 Для заданного языка определяет представление его грамматики,
 а также интерпретатор предложений этого языка.


 4) Итератор (Iterator):
 позволяет последовательно обойти элементы коллекции, не раскрывая внутренних деталей реализации.


 5) Посредник (Mediator):
 Инкапсулирует взаимодействие набора объектов которые ничего не знают друг о друге


 6) Хранитель (Memento):
 Предоставляет возможность восстановить объект в предыдущее состояние: Пример: модуль json, модуль pickle
 Позволяет вернуть предыдущее состояние объекта


 7) Наблюдатель (Observer):
 Определяет зависимость типа "один ко многим" между объектами таким образом,
 что при изменении состояния одного объекта все зависящие от него оповещаются об этом
 и автоматически обновляются

 # Пример: Django Signals(Сигналы), Flask Signals(Сигналы)

 8) Состояние (State):
 создания объектов, поведение которых изменяется при изменении состояния


 9) Стратегия (Strategy):
 Позволяет выбрать алгоритм во время выполнения.


 10) Шаблонный метод (Template method):
 --- CBV  -  Class-Based Views --- базовый класс - оставив реализацию некоторых шагов подклассам.  Django CBV


 11) Посетитель (Visitor):
 когда нужно применить функцию к каждому элементу коллекции: Пример - функция map()


"""










