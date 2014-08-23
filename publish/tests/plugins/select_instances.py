
import publish.lib
import publish.plugin


@publish.lib.log
class SelectInstances(publish.plugin.Selector):
    """Select instances"""

    hosts = ['python']
    version = (0, 1, 0)

    def process(self, context):
        for instance in ('inst1',):
            instance = publish.plugin.Instance(instance)

            for node in ('node1_PLY', 'node2_PLY', 'node3_GRP'):
                instance.add(node)

            for key, value in {'publishable': True,
                               'family': 'test',
                               'startFrame': 1001,
                               'endFrame': 1025}.iteritems():

                instance.config[key] = value

            context.add(instance)
