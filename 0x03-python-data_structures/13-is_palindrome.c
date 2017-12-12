#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of listint_t linked list
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	listint_t *end;
	int flag = 1;

	/* invalid or empty list */
	if (head == NULL || *head == NULL)
		return (0);
	end = (*head)->next;
	/* check 1 node */
	if (end == NULL)
		return (1);
	temp = *head;
	/* check 2 nodes */
	if (end->next == NULL && temp->n == end->n)
		return (1);
	while (end->next != NULL)
	{
		temp = end;
		end = end->next;
	}
	if ((*head)->n == end->n)
	{
		temp->next = NULL;
		flag = flag && is_palindrome(&(*head)->next);
		temp->next = end;
		return (flag);
	}
	return (0);
}
