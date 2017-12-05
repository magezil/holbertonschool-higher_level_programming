#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of linked list
 * @number: number to add
 *
 * Return: address of new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *prev;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	prev = NULL;
	for (current = *head; current != NULL && current->n < number; )
	{
		prev = current;
		current = current->next;
	}
	new->next = current;
	if (prev != NULL)
		prev->next = new;
	else
		*head = new;

	return (new);
}
