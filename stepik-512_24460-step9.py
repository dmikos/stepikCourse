#!/usr/bin/env python3

#https://stepik.org/lesson/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0-%D0%B8%D0%BC%D1%91%D0%BD-%D0%B8-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8-%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8-24460/step/9?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6766
"""
Ниже в комментариях было сказано, что задача решилась с первого раза при использовании конструкции
x = {'global' : {'parent' : None, 'vars' : []}}.
Воспользовался сегодня этой конструкцией, переписал весь код и программа заработала.
-
1. Циклом задаете количество строк, вводимых пользователем
2. Введенную строку разделяете на 3 переменные (условно cmd (которая может принимать значения add, create и get),
nsp (пространство имен указанное в строке) и arg (либо переменная для запросов add и get,
либо пространство имен родителя для запроса create))
3. Прописываете 3 функции:
    Функции add и create добавляют записи в словарь. Записываются в одну строку
    Функция get. Вот тут все проблемы. Возвращает  либо none, либо nsp, либо рекурсия и обращение к родительскому nsp.
"""
num = int(input("Enter number: "))

for i in range(num):
    print(i)
"""
NsStruct = {'global':[]}
def func(req, ns, var):
    if(req == "create"):
        print("request =", req, "\n", "namespace =", ns, ", parent =", var)
    elif (req == "add"):
        print("request =", req, "\n", "namespace =", ns, ", var =", var)
    elif (req == "get"):
        print("request =", req, "\n", "namespace =", ns, ", var =", var)
    print(NsStruct)
    print(NsStruct.keys())
    print("\n")
"""

if __name__ == "__main__":
    pass
#    func("add", "global", "a")
#    func("create", "foo", "global")
#    func("get", "foo", "a")
