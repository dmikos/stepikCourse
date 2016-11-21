#include <iostream>

int main()
{
  int i = 42;
  double d = 3.14;
  const char *s = "C-style string";
  double D = true;

  std::cout << "This is an integer " << i << "\n";
  std::cout << "This is a double " << d << "\n";
  std::cout << "This is a \"" << s << "\"\n";
  std::cout << "This is a BOOL type... \"" << D << "\"\n";

  return 0;
}