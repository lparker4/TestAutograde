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

@nbt.register(target="mult", label="Test mult function", score = 3, timeout = 1)
def test_mult(mult):
    assert mult(50, 6) == 300
    assert mult(7, 6) == 42
    assert mult(5, 8) == 40
    assert mult(9, 6) == 54
    assert mult(5, 6) == 30
    return 'well done 👌'

@nbt.register(target="dot", label="Test dot function", score = 2, timeout = 1)
def test_dot(dot):
    assert dot([5, 3], [6, 4]) == 42.0
    assert dot([5, 3], [6]) == 0.0
    return 'well done 👌'

@nbt.register(target="ind", label="Test ind function", score = 4, timeout = 1.5)
def test_ind(ind):
    assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
    assert ind(55, [55, 77, 42, 12, 42, 100]) == 0
    return 'well done 👌'
@nbt.register(target="letterScore", label="Test letterScore function", score = 4, timeout = 1.5)
def test_letter_score(letterScore):
    assert letterScore('c') == 3
    assert letterScore('^') == 0
    return 'well done 👌'
@nbt.register(target="scrabbleScore", label="Test scrabbleScore function", score = 4, timeout = 1.5)
def test_scrabble_score(scrabbleScore):
    assert scrabbleScore('quetzal') == 25
    assert scrabbleScore('jonquil') == 23
    return 'well done 👌'
@nbt.register(target="transcribe", label="Test transcribe function", score = 4, timeout = 1.5)
def test_transcribe_score(transcribe):
    assert transcribe("hello") == 'hello'
    assert transcribe("my name is annie") == 'my nume is unnie'
    return 'well done 👌'

@nbt.register(target="transform", label="Test transform function", score = 4, timeout = 1.5)
def test_transform_score(transform):
    assert transform("annie") == 'A for Annie! nnie'
    assert transform("aak") == 'A for Annie! A for Annie! k'
    return 'well done 👌'

@nbt.register(target="pigletLatin", label="Test piglet latin function", score = 4, timeout = 1.5)
def test_piglet_latin(pigletLatin):
    assert str(pigletLatin("be")).lower() == "ebay"
    return 'well done 👌'

@nbt.register(target="pigLatin", label="Test pig latin function", score = 4, timeout = 1.5)
def test_pig_latin(pigLatin):
    assert str(pigLatin('string')).lower() == 'ingstray'
    return 'well done 👌'
nbt.register_figure(target='SVGimage.svg', label='plot SVG')

nbt.register_figure(target='compose.svg', label='comp SVG')


# A few other special variables
@nbt.register(target=('__CONTEXT__', '__TEAM_MEMBERS__', '__COMMENTS__'), label='special variables')
def test_special_variables(context, team_members, comments):
    for member in team_members:
        print(f'Hello {member.first_name}')
    print()
    print(f'the tested notebook has {len(comments)} comments')
    #assert context.is_dir()

    
# `execute` brings a simple comand line interface, e.g.:
# `$ autograde -vvv test demo/test.py demo/ --context demo/context --target /tmp`
if __name__ == '__main__':
    sys.exit(nbt.execute())

