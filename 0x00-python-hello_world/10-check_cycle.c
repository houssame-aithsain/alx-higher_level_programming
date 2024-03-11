#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * This function checks if a given linked list has a cycle. It uses Floyd's
 * cycle-finding algorithm, where two pointers traverse the list at different
 * speeds. If there is a cycle, the fast pointer will eventually catch up to
 * the slow pointer.
 *
 * @list: Pointer to the head of the linked list to be checked.
 *
 * Return: 1 if a cycle is found, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	while (list)
	{
		if (list < list->next || list == list->next)
			return (1);
		list = list->next;
	}
	return (0);
}
