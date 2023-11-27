#!/usr/bin/env python3
import sys

from autograde import NotebookTest, ForgivingShell
from autograde.helpers import assert_raises

nbt = NotebookTest(
    'demo notebook test',  # title of the notebook test
    cell_timeout=4.,  # max duration per cell execution
    test_timeout=.1,  # max duration per test case execution
    shell_cls=ForgivingShell  # the shell class determines how to handle IPython special commands (`%...`, `!...`)
)

# an import filter can be any regular expression, e.g. r'autograde|networkx|typ.*'
nbt.set_import_filter(r'autograde', blacklist=True)


# Similarly, one may include figures into the report. Currently, PNG and SVG files are supported.
nbt.register_figure(target='plot.png', label='plot PNG')
nbt.register_figure(target='geek.png', label='geek PNG')

nbt.register_figure(target='SVGimage.svg', label='svg')
nbt.register_figure(target='does_not_exist.png', label='file not found')


# One may also load raw files from artifacts for more advanced testing
@nbt.register(target='__ARTIFACTS__', label='raw artifact')


# There are a few other special variables
@nbt.register(target=('__CONTEXT__', '__TEAM_MEMBERS__', '__COMMENTS__'), label='special variables')
def test_special_variables(context, team_members, comments):
    for member in team_members:
        print(f'Hello {member.first_name}')
    print()
    print(f'the tested notebook has {len(comments)} comments')
    assert context.is_dir()


# `execute` brings a simple comand line interface, e.g.:
# `$ autograde -vvv test demo/test.py demo/ --context demo/context --target /tmp`
if __name__ == '__main__':
    sys.exit(nbt.execute())
