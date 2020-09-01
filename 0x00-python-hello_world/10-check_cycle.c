#include "lists.h"
/**
 * check_cycle - checks all for students
 * @list: pointer
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *liebre = list;

	if (list == NULL)
		return (0);
	while (turtle != NULL && liebre != NULL && liebre->next != NULL)
	{
		turtle = turtle->next;
		liebre = liebre->next->next;
		if (turtle == liebre)
			return (1);
	}
	return (0);
}
