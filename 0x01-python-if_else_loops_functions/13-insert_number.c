#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert node
 * @head: pointer
 * @number: num
 * Return: void
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while ((current->next)->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
		/*(current->next) = new;*/
		/*new->next = (current->next)->next;*/
	}
	return (new);
}
