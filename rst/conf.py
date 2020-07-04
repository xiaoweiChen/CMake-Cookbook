# 这个文件是Sphinx配置文件
# 要查看所有配置，参阅：
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

#========================项目配置========================

project = 'CMake Cookbook'
#author = ''
language = 'zh_CN'

# 版本号, 包含alpha/beta/rc 标签
#release = '0.1'


#========================一般配置========================

# Sphinx的拓展配置

extensions = [
    # 添加markdown支持
    'recommonmark'
]

# 模板文件的路径，路径相对于此文件
templates_path = ['_templates']

# 忽略的路径/文件
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.virtualenv','README.md']

# 配置Sphinx支持的源文件格式
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

#========================HTML输出配置========================

#---------------------------主题配置-------------------------

# 默认主题配置
# https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
#html_theme = '默认主题为alabaster'


# sphinx_rtd_theme
# https://github.com/readthedocs/sphinx_rtd_theme

#extensions.append('sphinx_rtd_theme')
#html_theme = "sphinx_rtd_theme"


# Material Design HTML Theme for Sphinx
# https://github.com/myyasuda/sphinx_materialdesign_theme

html_theme = 'sphinx_materialdesign_theme'


# sphinx-material
# https://github.com/bashtage/sphinx-material

#import sphinx_material
#extensions.append('sphinx_material')
#html_theme = 'sphinx_material'
#html_theme_path = sphinx_material.html_theme_path()
#html_context = sphinx_material.get_html_context()


# sphinx-bootstrap-theme
# https://github.com/ryan-roemer/sphinx-bootstrap-theme

#import sphinx_bootstrap_theme
#html_theme = 'bootstrap'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()


# pallets-sphinx-themes
# https://github.com/pallets/pallets-sphinx-themes
# 可选 flask jinja werkzeug click

#extensions.append('pallets_sphinx_themes')
#html_theme = "flask"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

#========================PlantUML插件配置========================
# https://bitbucket.org/birkenfeld/sphinx-contrib/src/default/plantuml/
# https://plantuml.com
from os import path
extensions.append('sphinxcontrib.plantuml')
curPath = path.dirname(__file__)
plantuml = 'java -jar ' + curPath + '/.virtualenv/bin/plantuml.jar'
# 配置plantuml的输出格式（png或svg）
plantuml_output_format = 'svg'
# plantuml latex输出格式（eps、pdf或png）
# plantuml_latex_output_format = 'pdf'

#=======================latex pdf 配置===========================
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{xeCJK}
\setCJKmainfont[BoldFont=Noto Sans CJK SC]{Noto Sans CJK SC}
\setCJKsansfont[BoldFont=Noto Sans CJK SC]{Noto Sans CJK SC}
\setCJKmonofont{Noto Sans Mono CJK SC}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
\parindent 2em
\setcounter{tocdepth}{3}
'''
}
