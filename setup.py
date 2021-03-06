#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name="Django Autosave",
    version="0.7.10",
    author='Jason Goldstein',
    author_email='jason@betheshoe.com',
    url='https://github.com/theatlantic/django-autosave',
    packages=find_packages(),
    package_data={ 'autosave': ['static/autosave/js/*',] },
    description='Generic autosave for the Django Admin.',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
