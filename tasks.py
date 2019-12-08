import argparse
import subprocess
import setup_utils
import os


description = """
This is a simple python script to start the different tasks (e.g., test, publish, linters...).

We use this so that we can have common pipeline inside the continous integration and on
the local machine.

It is assumed that all python packages have already been installed (CI matrix or local).
"""


def task_test(args):
    """
    Command to run the unit tests
    """
    code = subprocess.call(['pytest', '--ignore=performance', '--cov-report=html', '--junitxml=reports/tests.xml', '--cov=pte'])
    exit(code)


def task_publish_and_bump_minor_version(args):
    """
    Command to bump minor version of a package and publish it
    """
    def parse_version(version):
        kvp = version.split('=')
        assert len(kvp) == 2
        version_str = kvp[1].split('.')
        assert len(version_str) == 3, f'Version must be defined as `major.minor.bugfix` format. Got={version_str}'
        return version_str

    # first parse the metadata and increment the minor version
    project_name = setup_utils.get_project_name()
    metadata_path = os.path.join('./src/', project_name, 'metadata.py')

    with open(metadata_path, 'r') as f:
        metadata = f.readlines()

    line_version = None
    for line_id, line in enumerate(metadata):
        if '__version__' in line:
            line_version = line_id
            break

    assert line_version is not None, f'can\'t publish. `__version__` tag can\'t be found in {metadata_path}'
    version = parse_version(metadata[line_version])
    version[1] = str(int(version[1]) + 1)
    version[2] = '0"'
    metadata[line_version] = '__version__ =' + '.'.join(version) + '\n'

    # now safely write the updated metadata to a temporary file
    metadata_new_path = metadata_path + '.new'
    with open(metadata_new_path, 'w') as f:
        for line in metadata:
            f.write(line)
    os.remove(metadata_path)
    os.rename(metadata_new_path, metadata_path)

    # prepare the package
    build_command = ['python', 'setup.py', 'sdist', 'bdist_wheel']
    code = subprocess.call(build_command)
    assert code == 0, f'command={build_command} failed with exit code={code}'

    # finally, publish the package
    publish_command = ['twine', 'upload', 'dist/*']
    code = subprocess.call(publish_command)
    assert code == 0, f'command={publish_command} failed with exit code={code}'
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
