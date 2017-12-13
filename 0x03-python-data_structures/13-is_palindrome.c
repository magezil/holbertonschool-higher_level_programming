#include "lists.h"

/**
 * add_nodeint - function adds a new node to the beginning of a listint_t list
 * @head: pointer to pointer to list
 * @n: n for new node
 *
 * Return: address to new element or NULL if failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	if (*head == NULL)
		new->next = NULL;
	else
		new->next = *head;
	*head = new;
	return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of listint_t linked list
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	listint_t *revhead;
	listint_t *rev;
	listint_t *hare;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	revhead = NULL;
	hare = *head;
	while (hare != NULL && hare->next != NULL)
	{
		revhead = add_nodeint(&revhead, temp->n);
		temp = temp->next;
		hare = hare->next->next;
	}
	if (hare != NULL && hare->next == NULL)
		temp = temp->next;
	rev = revhead;
	while (temp != NULL || rev != NULL)
	{
		if (temp->n != rev->n)
		{
			free_listint(revhead);
			return (0);
		}
		temp = temp->next;
		rev = rev->next;
	}
	free_listint(revhead);
	return (1);
}
