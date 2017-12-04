#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: singly linked list to check
 *
 * Return: 0 if no cycle, 1 if there is a cycle, -1 if error
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
		return (-1);

	slow = list;
	fast = list;
	while (fast->next != NULL)
	{
		if (fast->next->next == NULL)
			return (0);
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
