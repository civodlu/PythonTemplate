import argparse
import subprocess

description = """
This is a simple python script to start the different tasks (e.g., test, publish, linters...).

We use this so that we can have common pipeline inside the continous integration and on
the local machine.

It is assumed that all python packages have already been installed (CI matrix or local).
"""


def task_test(args):
    code = subprocess.call(['pytest', '--ignore=performance', '--cov-report=html', '--junitxml=reports/tests.xml', '--cov=pte'])
    exit(code)


parser = argparse.ArgumentParser(description=description)
parser.add_argument('--task', help='the name of the task to be performed')
parser.add_argument('--task_args', help='the argument of the task, encoded as semi colon separated key value pair '
                                        '(e.g., `key1:value1;key2:value2`)', default='')


args = parser.parse_args()
task_name = args.task

task_fn = locals().get(task_name)

if task_fn is None:
    raise RuntimeError('task={} was not found!'.format(task_name))

task_args = {}
for kvp in args.task_args.split(';'):
    if len(kvp) > 1:
        splits = kvp.split(':')
        assert len(splits) == 2, 'expected format `key:value`, got `{}`'.format(kvp)
        task_args[splits[0]] = splits[1]

task_fn(task_args)
