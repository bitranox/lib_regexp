import platform
import sys

# collect_ignore = ['build_docs.py', 'setup.py', 'dist.py']
collect_ignore = ['build_docs.py']


def pytest_cmdline_preparse(args):
    # run tests on multiple processes if pytest-xdist plugin is available
    if "xdist" in sys.modules:  # pytest-xdist plugin
        import multiprocessing

        num = int(max(multiprocessing.cpu_count() / 2, 1))
        args[:] = ["-n", str(num)] + args

    # add mypy option if not pypy
    if platform.python_implementation() != "PyPy":
        args[:] = ["--mypy"] + args
