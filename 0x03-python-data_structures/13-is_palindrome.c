#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to a pointer pointing to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
  listint_t *new_head, *slow, *fast, *prev_slow;
  listint_t *cut = NULL, *second_half, *it1, *it2;

  if (!head || !*head)
    return (1);

  new_head = *head;
  if (new_head->next != NULL)
    {
      for (fast = new_head, slow = new_head; fast != NULL && fast->next != NULL;
	   prev_slow = slow, slow = slow->next)
	fast = fast->next->next;
      if (fast != NULL)
	{
	  cut = slow;
	  slow = slow->next;
	}
      prev_slow->next = NULL;
      second_half = slow;
      it1 = reverse_listint(&second_half);
      for (it2 = *head; it2; it1 = it1->next, it2 = it2->next)
	{
	  if (it2->n != it1->n)
	    return (0);
	}
      if (cut == NULL)
	prev_slow->next = second_half;
      else
	{
	  prev_slow->next = cut;
	  cut->next = second_half;
	}
    }

  return (1);
}

/**
 * reverse_listint - Reverses a linked list in place
 * @head: Pointer to a pointer pointing to the head of the list
 *
 * Return: The new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
  listint_t *next_node = NULL, *prev_node = NULL;

  if (!head || !*head)
    return (NULL);

  while ((*head)->next)
    {
      next_node = (*head)->next;

      (*head)->next = prev_node;

      prev_node = *head;

      *head = next_node;
    }

  (*head)->next = prev_node;

  return (*head);
}

