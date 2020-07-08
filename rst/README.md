# 环境需求

- pandoc：用来转换文件

- Python 插件：`sphinx`、`sphinx-material`、`recommonmark`、`sphinx_materialdesign_theme`。这些依赖可以通过 pip 安装（conda 会有部分包找不到）

- 如果你希望生成 PDF，需要安装 texlive 环境和两个字体： `Noto Sans CJK SC` 和 `Noto Sans Mono CJK SC`

- 要生成 rst 文件，直接运行 `md2rst.py` 即可，但是一定要在本项目的顶级目录下运行

对于 Linux 和 MacOS 的用户来说，pandoc, texlive, noto fonts 可以通过对应平台的包管理器来安装（比如 apt, yum 或 homebrew）

而对于 windows 而言，pandoc, texlive, noto font。所有的这些软件可以在其对应的官网上找到。但是构建时需要将安装路径加入到 PATH 变量中

- [pandoc](https://www.pandoc.org/)
- [texlive](www.texlive.org)
- [noto font](http://www.google.cn/get/noto/)

# 文件生成

- 生成 html : linux 和 macos 直接切换到本目录下执行 `make html`， windows 执行 `./make.bat html`
- 生成 pdf: linux 和 macos 执行 `make latexpdf`， windows 执行 `./make.bat latexpdf`
- 生成 epub：执行 `make epub` 或 `./make.bat epub`