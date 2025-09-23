povtor={0}
def f(a,b):
    c = 0
    if((a,b) in povtor or(b,a) in povtor ):
        return 0
    average = (len(a) + len(b)) // 2
    for i in range(average):
        if a[i] != b[i]:
            c += 1
    print(f"Расстояние Хэминга :{c}")
    povtor.add((a, b))
    return c
def f1():
    u="0110101"
    ves=0
    for i in u:
        if(i!='0'):ves+=1
    print(f"Вес Хэминга для {u} - {ves}")
c=["0000","0101","1010","1111"]
d=0
print(len(c))
print(c)
for i in range(len(c)):
    for j in range(len(c)):
        if(c[i]!= c[j]):
            #print(f(c[i],c[j]))
            d+=(f(c[i],c[j]))
            print(f"{c[i]} | {c[j]}") #{f(c[i],c[j])}
print(f"Ответ: {d//(len(povtor)-1)}")

#4
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs): #cls - потому что -это класс , более понятное обозначение(общепринятое)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name="default"):
        self.name = name


# Проблема: __init__ вызывается каждый раз!
obj1 = Singleton("Первый")
obj2 = Singleton("Второй")
obj3 = Singleton("Третий")
print(obj1.name)  # "Второй" - перезаписалось!
print(obj2.name)
print(obj3.name)
#5
def st1():
    global q
    q=12134
    print(f"ДО {q}")
    st2()
def st2():
    q=123
    print(f"После {q}")
st1()
#6
def no_inherit(forbidden_class):
    """Декоратор, который запрещает наследование от указанного класса"""
    def init_subclass(cls, **kwargs):
        for base in cls.__bases__:
            if base is forbidden_class:
                raise TypeError(f"Наследование от {forbidden_class.__name__} запрещено!")

    forbidden_class.__init_subclass__ = classmethod(init_subclass)
    return forbidden_class
# Применяем декоратор к классу, от которого хотим запретить наследование
@no_inherit
class ForbiddenBase:
    pass
# Попытка наследования вызовет ошибку
try:
    class BadClass(ForbiddenBase):
        pass
except TypeError as e:
    print(f"Ошибка: {e}")

# Обычное наследование работает
class NormalClass:
    print("Успешно создан класс")
    pass
class GoodClass(NormalClass):
    pass
#7
def read_file(file_path):
    file = None
    try:
        file = open(file_path, 'r')
        data = file.read()
        print("Содержимое файла:", data)

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден!")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

    finally:
        if file:
            file.close()
            print("Файл закрыт")
read_file("sverla")
#8
def my_chain(*iterables):
    """Аналог itertools.chain - объединяет несколько итерируемых объектов в один поток"""
    for iterable in iterables:
        for item in iterable:
            yield item


# Пример использования
if __name__ == "__main__":
    # Тестируем на разных типах данных
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    tuple1 = (7, 8, 9)
    string = "abc"

    print("Объединяем списки, кортеж и строку:")
    for item in my_chain(list1, list2, tuple1, string):
        print(item, end=" ")
    # Вывод: 1 2 3 4 5 6 7 8 9 a b c

    print("\n\nТестируем с одним аргументом:")
    for item in my_chain([1, 2, 3]):
        print(item, end=" ")
    # Вывод: 1 2 3

    print("\n\nТестируем с пустыми итерируемыми объектами:")
    for item in my_chain([], [1, 2], (), "hi"):
        print(item, end=" ")
#8
class testDiscriptor:
    def __init__(self):
        self.zabot = 12
        print(self.zabot)
    def read(self):
        return (self.zabot/12)

    def __del__(self):

        delattr(self.zabot)
        print("Переменная удалена")
print(testDiscriptor)
#9
class LoggedAttribute:
    """Дескриптор, который логирует все операции с атрибутом"""

    def __init__(self, name=None):
        self.name = name
        self.value = None

    def __set_name__(self, owner, name):
        # Автоматически получаем имя атрибута
        if self.name is None:
            self.name = name

    def __get__(self, obj, objtype=None):
        # Логируем чтение атрибута
        if obj is None:
            # Вызывается из класса, а не из экземпляра
            print(f"LOG: Чтение атрибута {self.name} из класса")
            return self

        value = self.value
        # Используем id объекта вместо вызова __str__ чтобы избежать рекурсии
        print(f"LOG: Чтение атрибута {self.name} из экземпляра {id(obj)}: {value}")
        return value

    def __set__(self, obj, value):
        # Логируем запись атрибута
        old_value = self.value
        self.value = value
        print(f"LOG: Запись атрибута {self.name} в экземпляр {id(obj)}: {old_value} -> {value}")

    def __delete__(self, obj):
        # Логируем удаление атрибута
        print(f"LOG: Удаление атрибута {self.name} из экземпляра {id(obj)}")
        self.value = None


class Person:
    # Используем наш дескриптор
    name = LoggedAttribute()
    age = LoggedAttribute()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # Безопасное обращение к атрибутам через super() или прямое обращение к дескриптору
        return f"Person(name={self.__class__.name.value}, age={self.__class__.age.value})"


# Тестируем
if __name__ == "__main__":
    print("=== Создание экземпляра ===")
    PP = Person("Grigor", 123)

    print("\n=== Чтение атрибутов ===")
    print(f"Имя: {PP.name}")
    print(f"Возраст: {PP.age}")

    print("\n=== Вывод объекта ===")
    print(PP)
