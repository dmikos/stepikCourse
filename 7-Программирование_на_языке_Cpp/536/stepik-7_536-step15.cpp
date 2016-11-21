#include <iostream>
using namespace std;

int main()
{
    char c = '\0';
    while (cin.get(c))
    { // на каждой итерации считываем один символ в переменную c
        /* здесь можно пользоваться значением прочитанным в переменную c */
        if (c != 'a')
            cout << c; // выводим символ, если он не равен 'a'
    }

  return 0;
}
