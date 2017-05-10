"""Entrypoint for example application."""

import logging

from example.containers import Core, Models, WebHandlers, Application


if __name__ == '__main__':
    print(Models.users_manager().get_users())

    Core.config.update({
        'host': '127.0.0.1',
        'port': 9090,
        'debug': True,
    })
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG)

    app = Application.app_factory()

    # app.on_startup.append(init_pg)
    # app.on_cleanup.append(close_pg)

    app.router.add_get('/', WebHandlers.handle)

    Application.run_app(app)
