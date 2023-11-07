#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - Reverses a listint_t linked list.
 * @head: A pointer to the start of the listint_t.
 * Return: A pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * compare_lists - Compares two halves of a list.
 * @first_half: A pointer to the start of the first half.
 * @second_half: A pointer to the start of the second half.
 * Return: 1 if both halves are equal, 0 otherwise.
 */
int compare_lists(listint_t *first_half, listint_t *second_half)
{
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the beginning of the list.
 * Return: 1 if it is a palindrome, 0 if not.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *first_half, *second_half, *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = reverse_listint(&slow);
	first_half = *head;

	int is_pali = compare_lists(first_half, second_half);

	reverse_listint(&second_half);

	if (temp != NULL)
		temp->next = second_half;
	return (is_pali);
}
