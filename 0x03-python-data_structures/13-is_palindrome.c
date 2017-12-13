#include "lists.h"

/**
 * reverse_list - reverses a singly linked list
 * @head: head of listint_t linked list
 *
 * Return: head of reversed listint_t linked list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = NULL;
	while (head != NULL)
	{
		new = add_nodeint(&new, head->n);
		head = head->next;
	}
	return (new);
}

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

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	revhead = reverse_list(temp);
	rev = revhead;
	while (temp != NULL && rev != NULL)
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
