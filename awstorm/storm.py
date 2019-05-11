import sys
import boto3

from cliff.app import App
from cliff.commandmanager import CommandManager


class Awstorm(App):
    def __init__(self):
        super(Awstorm, self).__init__(
            description='A better cloudformation experience',
            version='0.0.2',
            deferred_help=True,
            command_manager=CommandManager('awstorm')
        )

    def initialize_app(self, argv):
        self.boto = boto3
        self.LOG.debug('initialize_app')


def main(argv=sys.argv[1:]):
    storm = Awstorm()
    return storm.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
