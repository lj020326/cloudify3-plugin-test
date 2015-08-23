cloudify-plugin-template
========================

* Master Branch [![Build Status](https://travis-ci.org/cloudify-cosmo/cloudify-plugin-template.svg?branch=master)](https://travis-ci.org/cloudify-cosmo/cloudify-plugin-template)

Cloudify plugin project template.

## Usage

See [Plugin Authoring Guide](http://getcloudify.org/guide/3.2/plugins-authoring.html)

## Tests

To run the example plugin tests, the included `dev-requirements.txt` should be installed.

```
pip install -r dev-requirements.txt
```

Then run the tests using nose

To run an integration/deploy test, then run the following commands 
from the blueprint directory (assuming you have a boostrapped manager already running):

cfy blueprints upload -b test-echo-plugin -p blueprint.yaml

cfy deployments create -b test-echo-plugin -d test-echo-plugin

cfy executions start -d test-echo-plugin -w install

Then in the cloudify manager logs & events, check to see if the following message is logged: 

ECHO PLUGIN: create running

If so, your plugin test has successfully deployed and run!


 
