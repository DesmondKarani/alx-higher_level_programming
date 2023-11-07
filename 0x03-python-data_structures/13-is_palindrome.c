#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int stack[2048]; /* Adjust size if you expect very large lists */
	int i = 0;

	/* An empty list is a palindrome */
	if (!current)
		return 1;


	/* Push all elements of the list into the stack*/
	while (current != NULL)
	{
		stack[i++] = current->n;
		current = current->next;
	}

	/* Check if the list is a palindrome */
	for (int j = 0; j < i / 2; j++)
	{
		if (stack[j] != stack[i - j - 1])
			return 0;
	}

	return 1;
}

