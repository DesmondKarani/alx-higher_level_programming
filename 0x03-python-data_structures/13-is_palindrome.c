#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next = NULL;
	int result = 1;

	if (head == NULL || *head == NULL) /* empty list is a palindrome */
		return (1);
	/* find the middle node of the list using slow and fast pointers */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	/* reverse the second half of the list */
	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	/* compare the first and second half of the list */
	slow = prev; /* slow now points to the last node */
	fast = *head; /* fast now points to the first node */
	while (slow)
	{
		if (slow->n != fast->n) /* mismatch found */
		{
			result = 0;
			break;
		}
		slow = slow->next;
		fast = fast->next;
	}
	/* restore the original list by reversing the second half again */
	prev = NULL;
	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	return (result);
}
