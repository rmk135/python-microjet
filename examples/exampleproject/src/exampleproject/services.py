"""Example project services module."""

from microjet import services


class Services(services.Catalog):
    """Catalog of service providers."""

    db_master = services.Provider(services.Postgresql)

    db_slave = services.Provider(services.Postgresql)

    redis = services.Provider(services.Redis)

    cassandra = services.Provider(services.Cassandra)

    rabbitmq = services.Provider(services.Rabbitmq)
