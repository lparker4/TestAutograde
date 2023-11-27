#!/usr/bin/env python3
import sys
import io
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



@nbt.register(target='biasedRandomWalk', label='biasedRandomWalk', timeout=10.)
def test_biasedWalk(biasedRandomWalk):
    num_moves = 10
    saved_stdout = sys.stdout
    try:
        out = io.StringIO()
        sys.stdout = out
        biasedRandomWalk(0.1, num_moves)
        output = str(out.getvalue().strip())
        print(output, file=saved_stdout, flush = True)
        moves = output.split(sep="\n")
        lefts = 0
        rights = 0
        for move in moves:
            # print(move)
            if move == "Left":
                lefts += 1
            elif move == "Right":
                rights += 1
        
        assert rights > lefts
        assert lefts != 0 and rights != 0
        assert len(moves) == num_moves
    finally:
        sys.stdout = saved_stdout


@nbt.register(target='experiment', label='experiment', score=2.5, timeout=10.)
def test_experiment(experiment):
    probability = 0.3
    distance = 5
    numTrials = 10
    exp=experiment(numTrials, probability, distance)

    assert len(exp) == numTrials

# this test only partially succeeds, returning a custom score
@nbt.register(target='surviveToReproduce', label='surviveToReproduce', score=3.)
def test_surviveToReproduce(surviveToReproduce):
    prob_p = 0.9
    prob_q = 0.1
    input = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
    output = surviveToReproduce(input, prob_p, prob_q)
    a = 0
    b = 0
    for i in range(len(output)):
        if output[i] == 'A':
            a += 1
        elif output[i] == 'B':
            b += 1
    assert a > b
    assert (a+b) <= len(input)

# Sometimes, the textual cells of a notebook are also of interest and should be included into the
# report. However, other than regular test cases, textual tests cannot be passed directly and are
# scored with NaN by default. Those test cases are supposed to be scored manually in audit mode.
# nbt.register_comment(target=r'\*Please write your essay here.\*', label='essay', score=4)
nbt.register_comment(target=r'\*A1:\*', label='Essay', score=4)


# Similarly, one may include figures into the report. Currently, PNG and SVG files are supported.
#nbt.register_figure(target='plot.png', label='plot PNG')
# nbt.register_figure(target='does_not_exist.png', label='file not found')


# One may also load raw files from artifacts for more advanced testing
# @nbt.register(target='__ARTIFACTS__', label='raw artifact')
# def test_raw_artifacts(artifacts):
    #assert artifacts.is_dir()
    # try:
    #     content1 = artifacts['figures\\fig_cell_5_1.png']
    #     return content1
    # except Exception as e:
    #     return False
    # try:
    #     content2 = artifacts['testcontent.txt'].decode('utf-8')
    # except Exception as e:
    #     return e        
    # return f'the following was read from a file: "{content2}"'


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
    try:
        sys.exit(nbt.execute())
    except Exception as e:
        print(e.args)
