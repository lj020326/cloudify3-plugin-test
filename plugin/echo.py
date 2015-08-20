
from cloudify import ctx
from cloudify.decorators import operation

@operation
def create(some_property, **kwargs ):
    msg = 'ECHO PLUGIN: create running'
    ctx.logger.info(msg)
    # setting node instance runtime property
    ctx.instance.runtime_properties['value_of_some_property'] = some_property

