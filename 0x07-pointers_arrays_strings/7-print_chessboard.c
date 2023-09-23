#include "main.h"

/*
 * print_cheeseboard - Entry point
 * @a: array
 * Return: Always 0 (Success)
 */
void print_cheeseboard(char (*a)[8])
{
	int i, n;

	for (i = 0; i < 8; i++)
	{
		for (n = 0; n < 8; n++)
			_putchar(a[i][n]);
		_putchar('\n');
	}
}
