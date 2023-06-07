#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @list_head: Pointer to the address of the head of the list
 * @number: Integer to be included in the new node
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **list_head, int number)
{
	listint_t *new_node, *current_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	if (*list_head == NULL || number <= (*list_head)->n)
	{
		new_node->n = number;
		new_node->next = *list_head;
		*list_head = new_node;
		return (new_node);
	}
	else
	{
		current_node = *list_head;
		while (current_node->next != NULL && number > current_node->next->n)
		{
			current_node = current_node->next;
		}
		new_node->n = number;
		new_node->next = current_node->next;
		current_node->next = new_node;
		return (new_node);
	}
	return (NULL);
}

