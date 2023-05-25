#include <Python.h>
#include <string.h>

static PyObject* cLink_strlen(PyObject* self, PyObject* args) {
	char* str;

	if (!PyArg_ParseTuple(args, "s", &str))
		return NULL;

    int size = 0;
    for (int i = 0;; i++)
    {
        if (str[i] & 0x80)
        {
            size++;
            i += 2;
        }

        else if (str[i] == '\0')
            break;

        else
            size++;
    }

	return Py_BuildValue("i", size - 1);
}


static PyMethodDef CLinkMethods[] = {
	{"strlen", cLink_strlen, METH_VARARGS, "count a string length."},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef cLinkmodule = {
	PyModuleDef_HEAD_INIT,
	"cLink",
	"It is a test module.",
	-1, CLinkMethods
};


PyMODINIT_FUNC PyInit_cLink(void) {
	return PyModule_Create(&cLinkmodule);
}