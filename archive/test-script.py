from autograde import NotebookTest, ForgivingShell
from autograde.helpers import assert_raises
import sys

nbt = NotebookTest(
    'sample notebook test',  # title of the notebook test
    cell_timeout=4.,  # max duration per cell execution
    test_timeout=.1,  # max duration per test case execution
    shell_cls=ForgivingShell  # the shell class determines how to handle IPython special commands (`%...`, `!...`)
)

# an import filter can be any regular expression, e.g. r'autograde|networkx|typ.*'
nbt.set_import_filter(r'autograde', blacklist=True)

@nbt.register(target="turnToDictionary", label="Test dictionary function", score = 3, timeout = 1)
def test_turn_to_dict(turnToDictionary):
    first = ["Apple", "Orange", "Banana", "Peach", "Pear"]
    second = ["Green", "Orange", "Yellow", "Pink", "Green"]
    assert turnToDictionary(first, second) == {'Apple': 'Green', 'Orange': 'Orange', 'Banana': 'Yellow', 'Peach': 'Pink', 'Pear': 'Green'}
    return 'well done 👌'

@nbt.register(target="tenLeapYears", label="Test leap year function", score = 2, timeout = 1)
def test_ten_leap_years(tenLeapYears):
    assert tenLeapYears() == [2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060]
    return 'well done 👌'

@nbt.register(target="toPigLatin", label="Test pig latin function", score = 4, timeout = 1.5)
def test_pig_latin(toPigLatin):
    assert str(toPigLatin("The quick brown fox")).lower() == "hetay uicqay rowbay oxfay"
    return 'well done 👌'

nbt.register_comment(target=r'\*A1:\*', label='Comment on difficulty', score=1)

# A few other special variables
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

