#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print information about a Python list
 *
 * @p: Pointer to a PyObject representing a list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t index;
	Py_ssize_t size = PyList_Size(p);
	PyListObject *listObj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %ld\n", listObj->allocated);

	for (index = 0; index < size; index++)
	{
		printf("Element %ld: %s\n",
		index, Py_TYPE(listObj->ob_item[index])->tp_name);
	}
}
