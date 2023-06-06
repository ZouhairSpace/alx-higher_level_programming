#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle
 * @head: Pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *ptr1;
	listint_t *prev_node;

	ptr1 = head;
	prev_node = head;
	while (head && ptr1 && ptr1->next)
	{
		head = head->next;
		ptr1 = ptr1->next->next;

		if (head == ptr1)
		{
			head = prev_node;
			prev_node =  ptr1;
			while (1)
			{
				ptr1 = prev_node;
				while (ptr1->next != head && ptr1->next != prev_node)
				{
					ptr1 = ptr1->next;
				}
				if (ptr1->next == head)
					break;

				head = head->next;
			}
			return (1);
		}
	}

	return (0);
}
