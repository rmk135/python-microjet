"""Example project application module."""

import yaml

import services


class Exampleproject:
    """Application."""

    services = services.Services

    def main(self):
        """Run application."""
        with open('/Users/romanmogilatov/'
                  '/ets-labs/python-microjet/examples/exampleproject/'
                  'etc/exampleproject.yaml', 'r') as config_file:
            config = yaml.load(config_file.read())

        self.services.init(config['services'])

        print(self.services.db_master().config)
        print(self.services.db_slave().config)
        print(self.services.redis().config)
        print(self.services.cassandra().config)
        print(self.services.rabbitmq().config)


Exampleproject().main()
