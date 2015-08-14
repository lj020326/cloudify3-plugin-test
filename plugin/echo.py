
from cloudify import ctx
from cloudify.decorators import operation

@operation
def create( **kwargs ):
    ctx.logger.info('ECHO PLUGIN: create running')

