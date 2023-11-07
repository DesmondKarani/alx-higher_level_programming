#include <Python.h>
#include <object.h>
#include <listobject.h>
#include "lists.h"

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject pointer to a Python list object.
 *
 * This function prints the size of the Python list, the amount of
 * allocated memory for the list, and the type of each element in the list.
 * If the provided PyObject is not a list, an error message is printed.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;

	/* Check if p is a list */
	if (PyList_Check(p))
	{
		size = PyList_GET_SIZE(p);
		allocated = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", allocated);

		/* Iterate over each element in the list and print its type */
		for (Py_ssize_t i = 0; i < size; i++)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "Invalid List Object\n");
	}
}
