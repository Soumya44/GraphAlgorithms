// CPP code to find vertices in a fibonacci
// cube graph of order n
#include<iostream>
using namespace std;

// function to find fibonacci number
int fib(int n)
{
	if (n <= 1)
		return n;
	return fib(n - 1) + fib(n - 2);
}

// function for finding number of vertices
// in fibonacci cube graph
int findVertices (int n)
{
	// return fibonacci number for f(n + 2)
	return fib(n + 2);
}

// driver program
int main()
{
	// n is the order of the graph
	int n = 3;
	cout << findVertices(n);
	return 0;
}
