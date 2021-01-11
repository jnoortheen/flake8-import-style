import ast

import pkg_resources


__version__ = pkg_resources.get_distribution(__package__).version

I901 = "I901 use 'import {module} as tp' instead of 'from {module} import {names}'"
I902 = "I902 use 'import {module} as tp' instead of 'import {names}'"


class I9(object):
    """Complain about all "from x import y" style imports."""

    name = "typing-import-style"
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for i in ast.walk(self.tree):
            if isinstance(i, ast.ImportFrom):
                if i.module == "typing":
                    message = I901.format(
                        module=(i.module or "..."),
                        names=", ".join(i.name for i in i.names),
                    )
                    yield (i.lineno, i.col_offset, message, "I901")
            elif isinstance(i, ast.Import) and i.names:
                module = i.names[0]
                if module.name == "typing" and module.asname != "tp":
                    message = I902.format(
                        module="typing",
                        names=", ".join(i.name for i in i.names),
                    )
                    yield (i.lineno, i.col_offset, message, "I902")
