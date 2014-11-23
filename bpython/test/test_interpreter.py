import unittest

from bpython.curtsiesfrontend import interpreter
from bpython.curtsiesfrontend.repl import bad_empty_lines_removed
from curtsies.fmtfuncs import *

class TestInterpreter(unittest.TestCase):
    def test_syntaxerror(self):
        i = interpreter.Interp()
        a = []

        def append_to_a(message):
            a.append(message)
        
        i.write = append_to_a
        i.runsource('1.1.1.1')

        expected = ''+u''+u'  File '+green(u'"<input>"')+u', line '+bold(magenta(u'1'))+u'\n'+u'    '+u'1.1'+u'.'+u'1.1'+u'\n'+u'    '+u'    '+u'^'+u'\n'+bold(red(u'SyntaxError'))+u': '+cyan(u'invalid syntax')+u'\n'

        self.assertEquals(str(plain('').join(a)), str(expected))
        self.assertEquals(plain('').join(a), expected)

    def test_traceback(self):
        i = interpreter.Interp()
        a = []

        def append_to_a(message):
            a.append(message)
        
        i.write = append_to_a

        def f():
            return 1/0

        def g():
            return f()

        i.runsource('g()')

        expected = u'Traceback (most recent call last):\n'+''+u'  File '+green(u'"<input>"')+u', line '+bold (magenta(u'1'))+u', in '+cyan(u'<module>')+u'\n'+''+bold(red(u'NameError'))+u': '+cyan(u"name 'g' is not defined")+u'\n'

        self.assertEquals(str(plain('').join(a)), str(expected))
        self.assertEquals(plain('').join(a), expected)

class TestPreprocessing(unittest.TestCase):
    def test_bad_empty_lines_removed(self):
        self.assertEqual(add_or_remove_blank_lines("def foo():\n"
                                             "    return 1\n"
                                             "\n"
                                             "    pass\n"),
                         "def foo():\n"
                         "    return 1\n"
                         "    pass\n")

    def test_add_line(self):
        self.assertEqual(add_or_remove_blank_lines("def foo():\n"
                                             "    return 1\n"
                                             "1\n"),
                         "def foo():\n"
                         "    return 1\n"
                         "\n",
                         "1\n")


