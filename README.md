# pyxstr2swift
Python package for a Xcode strings file to a swift localized string file

For example,
```swift
import Foundation

struct Localized {
  static let edit = "edit".localized // edit
}

```

It is available in python2.7 and python3

```console
foo@bar:~$ pip install -U pyxstr2swift
```

```console
foo@bar:~$ xstr2swift [-f] [-m] [source_path] [target_path] [struct_name]
foo@bar:~$ python -m pyxstr2swift.pyxstr2swift [-f] [-m] [source_path] [target_path] [struct_name]
```

For using it, you should import a string extension library or write it.
Below the library help you to use it easily.
https://github.com/ocworld/OHSwiftLocalizedString


To use it in Xcode build pharses,
1. Install this module using python PIP.
If pip is not installed on your device, this command helps you. 

```console
foo@bar:~$ brew install python
foo@bar:~$ pip3 install -U pyxstr2swift
```

2. Add a output swift file to your project
3. Add a strings file to your project and write string keys and values
4. Add Run Script to build pharses before Compile Sources
5. Change Shell /bin/sh to /bin/bash (or /bin/zsh)
6. Write shell command.
For example,
```console
xstr2swift -f -m "${SRCROOT}/Your project/en.lproj/Localized.strings" "${SRCROOT}/Your project/Localized.swift" "Localized"
```

7. That' all! build Your project now!

Thanks to an author of this post https://medium.com/ios-forever/ios에서-localization하는-gorgeous-한-방법-f82ac29d2cfe
