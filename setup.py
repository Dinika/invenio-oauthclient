# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016, 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio module that provides OAuth web authorization support."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'SQLAlchemy-Continuum>=1.2.1',
    'check-manifest>=0.25',
    'coverage>=4.0',
    'httpretty>=0.8.14',
    'invenio-accounts>=1.0.0b8',
    'invenio-userprofiles>=1.0.0b2',
    'isort>=4.2.2',
    'mock>=1.3.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.3',
    'simplejson>=3.8',
]

extras_require = {
    'admin': [
        'invenio-admin>=1.0.0b3',
    ],
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'github': [
        'github3.py>=1.0.0a4',
        'uritemplate.py>=0.2.0,<2.0',
    ],
    'mysql': [
        'invenio-db[mysql]>=1.0.0b8',
    ],
    'orcid': [],
    'postgresql': [
        'invenio-db[postgresql]>=1.0.0b8',
    ],
    'sqlite': [
        'invenio-db>=1.0.0b8',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name in ('mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=2.6.2',
]

install_requires = [
    'Flask-BabelEx>=0.9.3',
    'Flask-Breadcrumbs>=0.3.0',
    'Flask-OAuthlib>=0.9.3',
    'Flask>=0.11.1',
    'blinker>=1.4',
    'invenio-accounts>=1.0.0b12',
    'invenio-accounts>=1.0.0b7',
    'invenio-mail>=1.0.0b1',
    'six>=1.9',
    'sqlalchemy-utils>=0.32.0',
    'uritools>=1.0.1',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_oauthclient', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-oauthclient',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio oauth authentication',
    license='GPLv2',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-oauthclient',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_admin.views': [
            'invenio_oauth_remote_account = '
            'invenio_oauthclient.admin:remote_account_adminview',
            'invenio_oauth_remote_token = '
            'invenio_oauthclient.admin:remote_token_adminview',
            'invenio_oauth_user_identity = '
            'invenio_oauthclient.admin:user_identity_adminview',
        ],
        'invenio_base.apps': [
            'invenio_oauthclient = invenio_oauthclient:InvenioOAuthClient',
        ],
        'invenio_base.api_apps': [
            'invenio_oauthclient = invenio_oauthclient:InvenioOAuthClient',
        ],
        'invenio_base.blueprints': [
            'invenio_oauthclient = invenio_oauthclient.views.client:blueprint',
            'invenio_oauthclient_settings = '
            'invenio_oauthclient.views.settings:blueprint',
        ],
        'invenio_db.alembic': [
            'invenio_oauthclient = invenio_oauthclient:alembic',
        ],
        'invenio_db.models': [
            'invenio_oauthclient = invenio_oauthclient.models',
        ],
        'invenio_base.secret_key': [
            'invenio_oauthclient = '
            'invenio_oauthclient.utils:rebuild_access_tokens',
        ],
        'invenio_i18n.translations': [
            'invenio_oauthclient = invenio_oauthclient',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 4 - Beta',
    ],
)
