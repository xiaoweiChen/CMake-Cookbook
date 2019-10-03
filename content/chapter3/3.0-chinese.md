# 第3章 检测外部库和程序

本章中主要内容有:

* 检测Python解释器
* 检测Python库
* 检测Python模块和包
* 检测BLAS和LAPACK数学库
* 检测OpenMP并行环境
* 检测MPI并行环境
* 检测Eigen库
* 检测Boost库
* 检测外部库:Ⅰ. 使用pkg-config
* 检测外部库:Ⅱ. 书写find模块

我们的项目常常会依赖于其他项目和库。本章将演示，如何检测外部库、框架和项目，以及如何链接到这些库。CMake有一组预打包模块，用于检测常用库和程序，例如：Python和Boost。可以使用`cmake --help-module-list`获得现有模块的列表。但是，不是所有的库和程序都包含在其中，有时必须自己编写检测脚本。本章将讨论相应的工具，了解CMake的`find`族命令:

* **find_file**：在相应路径下查找命名文件
* **find_library**：查找一个库文件
* **find_package**：从外部项目查找和加载设置
* **find_path**：查找包含指定文件的目录
* **find_program**：找到一个可执行程序

**NOTE**:*可以使用`--help-command`命令行显示CMake内置命令的打印文档。*

