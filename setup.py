# ------------------------------------------------------------------------------
#  Created by Tyler Stegmaier.
#  Property of TrueLogic Company.
#  Copyright (c) 2020.
# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------
import os

from setuptools import setup

from Extensions import __author__, __classifiers__, __email__, __license__, __maintainer__, __maintainer_email__, __name__, __short_description__, __url__, __version__
from Extensions.Setup import *
from Extensions.debug import *



long_description = ReadFromFile(os.path.abspath("./PyPiReadme.md"))

install_requires = GetRequirements(os.path.abspath('./requirements.txt'))

_packages, _package_data = Get_Packages_Data(os.path.abspath('./Extensions'), __name__, includes=MatchFileTypes('py', 'png'))

PrettyPrint('_packages', _packages)
PrettyPrint('_package_data', _package_data)


setup(name=__name__,
      version=__version__,
      packages=_packages,
      url=__url__,
      license=__license__,
      author=__author__,
      author_email=__email__,
      maintainer=__maintainer__,
      maintainer_email=__maintainer_email__,
      description=__short_description__,
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=install_requires,
      classifiers=__classifiers__,
      keywords=f'{__name__} Tkinter Extensions tk ttk tkinter',
      package_dir={ f'{__name__}': f'src/{__name__}' },
      package_data=_package_data,
      )