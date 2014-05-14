from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README.rst')).read()
#NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.2'

install_requires = [
    'jinja2',
    'webob',
    'pydap >=3.2.1'
]


setup(name='pydap.responses.html',
    version=version,
    description="A handler that generates an html form for downloading data from Pydap",
#long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='html opendap pydap dap data access',
    author='Roberto De Almeida',
    author_email='roberto@dealmeida.net',
#url='http://pydap.org/handlers.html#csv',
    dependency_links = ['https://github.com/pacificclimate/pydap-pdp/tarball/master#egg=Pydap-3.2.2'],
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    package_data={'pydap.responses.html': ['templates/*.html']},
    namespace_packages = ['pydap', 'pydap.responses'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
        [pydap.response]    
        html = pydap.responses.html:HTMLResponse
    """,
)
