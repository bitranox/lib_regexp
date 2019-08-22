import sys

# collect_ignore = ['build_docs.py', 'setup.py', 'dist.py']
collect_ignore = ['build_docs.py']


def pytest_load_initial_conftests(args):
    # run tests on multiple processes if pytest-xdist plugin is available
    if "xdist" in sys.modules:  # pytest-xdist plugin
        import multiprocessing

        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args
