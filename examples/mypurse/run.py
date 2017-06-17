"""Application run script."""

import datetime
import logging
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'src'))  # noqa

from mypurse.app import Core, Profile

async def main():
    """Main function."""
    profile = await Profile.registration_service().register(
        first_name='Roman',
        last_name='Mogylatov',
        birth_date=datetime.date(year=1988, month=5, day=4),
        password='secret123')
    print(profile)
    print('Full name', profile.info.full_name)
    print('Age', profile.info.age)

    try:
        await Profile.updater_service().update_info(profile,
                                                    first_name='',
                                                    last_name='',)
    except RuntimeError as exception:
        print(exception)

if __name__ == '__main__':
    Core.config.update({
        'thread_pool_size': 4,
        'host': '127.0.0.1',
        'port': 9090,
        'debug': True,
    })
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG)

    Core.loop().run_until_complete(main())
