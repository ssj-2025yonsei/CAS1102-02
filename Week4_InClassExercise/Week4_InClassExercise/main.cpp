// This is for Exercise 2

#include <iostream>
#include "math.h"
int main()
{
	int a;
	int b;

	std::cout << "Enter an integer: ";
	std::cin >> a;
	std::cout << "Enter an integer: ";
	std::cin >> b;
	std::cout << add(a, b) << std::endl;
	
	std::cout << "Enter an integer: ";
	std::cin >> a;
	std::cout << "Enter an integer: ";
	std::cin >> b;
	std::cout << multiply(a, b) << std::endl;

	int c;

	std::cout << "Enter an integer: ";
	std::cin >> a;
	std::cout << "Enter an integer: ";
	std::cin >> b;
	std::cout << "Enter an integer: ";
	std::cin >> c;
	std::cout << add(a, b, c) << std::endl;

	double d;
	double e;

	std::cout << "Enter a double: ";
	std::cin >> d;
	std::cout << "Enter a double: ";
	std::cin >> e;
	std::cout << add(d, e) << std::endl;
}