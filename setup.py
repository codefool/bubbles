# setup script for bubbles

from distutils.core import setup
from bubbles import __version__

setup(
        name='bubbles',
        version=__version__,
        description='bubbles: a simple dynamic SOAP library',
        author='Chris Frantz',
        author_email='chris.frantz@hp.com',
        url='http://github.com/cfrantz/bubbles',
        packages=['bubbles', 'bubbles.soap', 'bubbles.util', 'bubbles.xsd'],
        license='LGPL_v2.1',
)



# vim: ts=4 sts=4 sw=4 expandtab:
