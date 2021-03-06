from setuptools import setup

tests_require = [
    'django',
]

setup(
    name='django-mailbox',
    version='2.1.1',
    url='http://bitbucket.org/latestrevision/django-mailbox/',
    description=(
        'Import mail from POP3, IMAP, local mailboxes or directly from '
        'Postfix or Exim4 into your Django application automatically.'
    ),
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='django_mailbox.runtests.runtests',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Email :: Post-Office',
        'Topic :: Communications :: Email :: Post-Office :: IMAP',
        'Topic :: Communications :: Email :: Post-Office :: POP3',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
    ],
    packages=[
        'django_mailbox',
        'django_mailbox.management',
        'django_mailbox.management.commands',
        'django_mailbox.migrations',
        'django_mailbox.transports',
        'django_mailbox.tests',
    ],
    install_requires=[
        'six'
    ]
)
