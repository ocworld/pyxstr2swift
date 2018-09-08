# pyxstr2swift

[![PyPI version shields.io](https://img.shields.io/pypi/v/ansicolortags.svg)](https://pypi.org/project/pyxstr2swift/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.org/project/pyxstr2swift/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Description

Python package for a Xcode strings file to a swift localized string file

For example,

```
/* 
  Localizable.strings

  Created by Keunhyun Oh on 2018. 8. 15..
  Copyright © 2018년 Keunhyun Oh. All rights reserved.
*/

test = "test_value";

```

to

```swift
import Foundation

struct Localizable {
  static let test = NSLocalizedString("test", tableName: "Localizable", comment: "") // test_value
}

```

It is available in python2.7, 3.4, 3.5, 3.6, and 3.7

```bash
foo@bar:~$ pip install -U pyxstr2swift
```

```bash
foo@bar:~$ xstr2swift [-h] [--st STRUCTNAME] [-f] [-m] [-v] source target
foo@bar:~$ python -m pyxstr2swift.xstr2swift [-h] [--structname STRUCTNAME] [-f] [-m] source target
```


To use it in Xcode build pharses,
1. Install this module using python PIP.
If pip is not installed on your device, this command helps you. 

```bash
foo@bar:~$ brew install python
foo@bar:~$ pip3 install --upgrade pyxstr2swift
```

or

install anaconda and set configures
https://www.anaconda.com/download/

2. Add a output swift file to your project
3. Add a strings file to your project and write string keys and values
4. Add Run Script to build pharses before Compile Sources
5. Change Shell /bin/sh to /bin/bash (or /bin/zsh)
6. Write shell command.
For example,
```bash
#If you use anaconda, anaconda3/bin should be added to path
#export PATH="${HOME}/anaconda3/bin:$PATH"
pip install --upgrade pyxstr2swift
xstr2swift -f -m "${SRCROOT}/Your project/en.lproj/Localizable.strings" "${SRCROOT}/Your project/Localizable.swift"
```

My project's shell command is that
```bash
# .bash_profile includes export PATH="${HOME}/anaconda3/bin:$PATH"
source ~/.bash_profile

# a conda env is already created that name is iosdev
conda activate iosdev
pip install --upgrade pyxstr2swift
xstr2swift -f -m "${SRCROOT}/My Project/en.lproj/Localizable.strings" "${SRCROOT}/My Project/Localizable.swift"
conda deactivate
```

7. That' all! build Your project now!

```bash
usage: xstr2swift [-h] [-st STRUCTNAME] [-f] [-m] [-v] source target

pyxstr2swift needs arguments

positional arguments:
  source                source: a strings file
  target                target: a swift file

optional arguments:
  -h, --help            show this help message and exit
  -st STRUCTNAME, --structname STRUCTNAME
                        structname: a struct name in a target file
  -f, --force           force to write a target file if already exist
  -m, --comment         values are added as comment
  -v, --verbose         Display console output
```

## Test
unittest on python 2.7, 3.4, 3.5, 3.6, 3.7

## References
- https://medium.com/ios-forever/ios에서-localization하는-gorgeous-한-방법-f82ac29d2cfe
Thanks to an author of this post
- https://github.com/ocworld/OHSwiftLocalizedString
It is help you to use localized strings
