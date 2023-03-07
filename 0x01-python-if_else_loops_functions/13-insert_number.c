#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * insert_node - that inserts a number into a sorted singly linked list
 * @head: double pointer, pointer to the pointer to a node (struct)
 * @number = value stored in the node
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *prev = *head;
	listint_t *current = (*head)->next;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;

	if (current == NULL)
	{
		if (number > prev->n)
			prev->next = new_node;
		else
		{
			new_node->next = *head;
			*head = new_node;
		}
	}
	while (current != NULL)
	{
		if (number <= current->n)
		{
			new_node->next = current;
			prev->next = new_node;
			break;
		}
		if (current->next == NULL)
		{
			current->next = new_node;
			new_node->next = NULL;
			break;
		}
		current = current->next;
		prev = prev->next;
	}
	return (new_node);
}
