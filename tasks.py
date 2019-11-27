import argparse

description = """
This is a simple python script to start the different tasks (e.g., test, publish, linters...).

We use this so that we can have common pipeline inside the continous integration and on
the local machine.

It is assumed that all python packages have already been installed (CI matrix or local).
"""

parser = argparse.ArgumentParser(description=description)
parser.add_argument('--task', help='the name of the task to be performed')
parser.add_argument('--task_args', help='the argument of the task, encoded as semi colon separated key value pair '
                                        '(e.g., `key1:value1;key2:value2`)', default='')


args = parser.parse_args()
task_name = args.task

task_fn = locals().get(task_name)

if task_fn is None:
    raise RuntimeError('task={} was not found!'.format(task_name))

raise NotImplemented()