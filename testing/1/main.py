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
