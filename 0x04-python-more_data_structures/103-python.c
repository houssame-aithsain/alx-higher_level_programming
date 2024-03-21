#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(bytes))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyUnicode_1BYTE_DATA(bytes));

	printf("  first %ld bytes:", size > 10 ? 10 : size);

	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf(" %02hhx", bytes->ob_sval[i]);
	}

	printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, i;
	const char *type;

	size = Py_SIZE(list);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
