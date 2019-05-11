import os
import logging

from cliff.command import Command
from pathlib import Path
from colorama import Fore


class Initialize(Command):
    "Go go go!"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Initialize, self).get_parser(prog_name)
        parser.add_argument('base_directory', nargs='?', default='.')
        return parser

    def take_action(self, parsed_args):
        out = self.app.stdout
        self.log.debug('Args: '+str(parsed_args))
        base_dir = parsed_args.base_directory
        directories = ['cloudformation/parameters', 'doc', 'scripts']

        out.write(Fore.GREEN + 'Creating structure:\n')

        for directory in directories:
            try:
                path = os.path.join(base_dir, directory)
                out.write(Fore.YELLOW+'Creating: '+path+'\n')
                os.makedirs(path)
            except OSError as err:
                self.log.debug(err)
                out.write(Fore.RED+'Received an error quiting...\n'+Fore.RESET)

        out.write(Fore.YELLOW+'Adding Readme\n')
        Path(os.path.join(base_dir, 'Readme.md')).touch()

        out.write(Fore.GREEN + 'Done! Enjoy your project.\n')
