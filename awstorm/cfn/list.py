import logging

from cliff.command import Command
from cliff.lister import Lister


class Local(Command):
    "List local cloudformation stacks"
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.app.stdout.write('test\n'+str(parsed_args))


class Remote(Lister):
    "List remote cloudformation stacks"
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        cfn = self.app.boto.client('cloudformation')
        stacks = cfn.list_stacks()['StackSummaries']

        return (
            ('Name', 'Status', 'Last Updated',),
            ((stack['StackName'], stack['StackStatus'],
              stack.get('LastUpdatedTime', 'N/A'),) for stack in stacks)
        )
