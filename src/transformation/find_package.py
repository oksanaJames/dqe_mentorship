import importlib
import argparse

"""
Simple package installation check. If package isn't installed message should be printed.
If package is found then package information (__doc__) should be printed.
"""


def check_module(module_name):
    # search if package is installed
    package_spec = importlib.util.find_spec(module_name)

    if package_spec is None:
        print(f"Package: '{module_name}' not found")
    else:
        package_path = package_spec.loader.load_module()
        print(f"Package '{module_name}' found,  __doc__: {package_path.__doc__}")


def parse_cmd_args():
    package_help = "Package name to check"

    parser = argparse.ArgumentParser()
    parser.add_argument('package', help=package_help)

    cmd, _ = parser.parse_known_args()
    return cmd.package


if __name__ == '__main__':
    args = parse_cmd_args()
    check_module(args)

