import importlib
import logging
from importlib.metadata import version
import argparse

"""
Package installation check with logging to console and file simultaneously with separate LOG LEVELS for each.
If package isn't installed ERROR should be logged.
If package is found then package information (__doc__) should be printed in WARNING level. Path to file in INFO and
package version in DEBUG mode.
"""


level_config = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING}
log_filename = 'basic.log'
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s',
                                  datefmt='%d/%m/%Y %H:%M:%S')


def check_module(module_name, cmd_level, file_level):
    # search if package is installed
    package_spec = importlib.util.find_spec(module_name)

    # create file handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(level_config[file_level.lower()])

    # create console handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(level_config[cmd_level.lower()])

    logger = logging.getLogger('root')
    logger.setLevel(level_config[file_level.lower()])

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    if package_spec is None:
        logger.error("Package: '{}' not found".format(module_name))
    else:
        package_path = package_spec.loader.load_module()
        logger.info("Package '{}' path: {}\n".format(module_name, package_path))
        logger.warning("Package '{}' __doc__: {}\n".format(module_name, package_path.__doc__))
        logger.debug("Package '{}' version: {}".format(module_name, version(module_name)))


def parse_cmd_args():
    package_help = "Package name to check"
    file_level_help = "Set LOG LEVEL for file output"
    cmd_level_help = "Set LOG LEVEL for cmd output"

    parser = argparse.ArgumentParser()
    parser.add_argument('package', help=package_help)
    parser.add_argument('file_level', help=file_level_help, default='INFO')
    parser.add_argument('cmd_level', help=cmd_level_help, default='INFO')

    cmd, _ = parser.parse_known_args()
    return cmd.package, cmd.file_level, cmd.cmd_level


if __name__ == '__main__':
    args = parse_cmd_args()
    check_module(*args)

