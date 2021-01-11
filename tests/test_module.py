import ast
import unittest

import flake8_typing_import_style


class I8Test(unittest.TestCase):

    def test_run(self):
        tree = ast.parse("import typing")
        i8 = flake8_typing_import_style.I9(tree)
        self.assertEqual(list(i8.run()), [(1, 0, "I902 use 'import typing as tp' instead of 'import typing'", 'I902')])

        tree = ast.parse("import typing as tp")
        i8 = flake8_typing_import_style.I9(tree)
        self.assertEqual(list(i8.run()), [])

        tree = ast.parse("from typing import obj")
        i8 = flake8_typing_import_style.I9(tree)
        self.assertEqual(list(i8.run()), [(
            1,
            0,
            "I901 use 'import typing as tp' instead of 'from typing import obj'",
            "I901",
        )])
