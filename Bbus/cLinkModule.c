#include <Python.h>
#include <string.h>

static PyObject* cLink_strlen(PyObject* self, PyObject* args) {
	char* str;

	if (!PyArg_ParseTuple(args, "s", &str))
		return NULL;

    int size = 0;
    for (int i = 0;; i++)
    {
        if (str[i] & 0x80)     // �ѱ��̴�! �迭 �ν��� Ű�� i�� 1���� ������Ű��!
        {
            size++;
            i += 2;
        }

        else if (str[i] == '\0')  // ���ڿ��� ���̴�! '' �̴�! ����~
            break;

        else                    // �ƴϸ� �Ϲ� �ƽ�Ű�� �����ϰ� ������ 1 ����!
            size++;
    }

	return Py_BuildValue("i", size - 1);
}

// 3. ��⿡ ����� �Լ� ���Ǹ� ���� �迭(__dict__ �Ӽ��� ��)
static PyMethodDef CLinkMethods[] = {
	{"strlen", cLink_strlen, METH_VARARGS, "count a string length."},
	{NULL, NULL, 0, NULL} // <- �迭 �� ǥ��.
};

static PyModuleDef cLinkmodule = { //2. ������ ��� ������ ��� ����ü
	PyModuleDef_HEAD_INIT,
	"cLink",
	"It is a test module.",
	-1, CLinkMethods //3. CLinkMethods �迭 ����
};

//1. ���̽� ���������Ϳ��� import�� �� ���� (PyInit_<module> �Լ�)
PyMODINIT_FUNC PyInit_cLink(void) {
	return PyModule_Create(&cLinkmodule); //2. cLinkmodule ����ü ����
}