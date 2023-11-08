#include <Python.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A PyObject pointer to the Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	printf("[*] Python list info\n");
	/* Check if p is a list object */
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	/* Get the size and the allocated size of the list */
	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	/* Iterate over the elements of the list */
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A PyObject pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *buffer;

	printf("[.] bytes object info\n");
	/* Check if p is a bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	/* Get the size and the buffer of the bytes object */
	size = PyBytes_Size(p);
	buffer = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);
	/* Print the first 10 bytes of the buffer */
	if (size < 10)
		printf("  first %ld bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");
	for (i = 0; i <= size && i < 10; i++)
		printf("%02hhx ", buffer[i]);
	printf("\n");
}
