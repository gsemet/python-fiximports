
##################
Python Fix Imports
##################

Python Fix Imports is a Sublime Text 3 plugin ...

Rationals
*********


Installation
************

To avoid dependencies, all necessary modules are included within the package.

1. Using ``Sublime Package Control``

  - Use ``cmd+shift+P`` shortcut then ``Package Control: Install Package``
  - Look for ``Python Fix Imports`` and install it.

2. Using Git repository on GitHub:

  - Open a terminal, move to Packages directory (refers to the folder that opens when you use the
    ``Preferences > Browse Packages``... menu).
  - Then type in terminal::

    `git clone https://github.com/Stibbons/python-fiximports python_fiximports'`

Settings
********

Global Settings
===============

You'll find settings in Preferences menu (``Preferences -> Package Settings -> Python Fix Imports``).

::

    {
        // Automatically fix the imports on save
        "autofix_on_save": false,

        // Enable or disabl split of every imports in own line (one object import per line)
        "split_import_statements": true,

        // Enable or disabl sorting or import in its own group
        "sort_import_statements": true,
    }


Per-project settings
====================

::

    {
        "settings": {
            "python_fiximports": {
                "autofix_on_save": true
            }
        }
    }

By editing ``User settings``, your personal liking will be kept safe over plugin upgrades.

Usage
*****

Formatting is applied on the whole document.

Using keyboard:
===============

- GNU/Linux: ``ctrl+shift+i``
- OSX:       ``ctrl+shift+i``
- Windows:   ``ctrl+shift+i``

SideBar
=======

Right click on the file(s) or folder(s)

On Save
=======

Imports are reorganized automatically on save if the following setting is set: ``autofix_on_save``.

Command Palette
===============

Bring up the Command Palette and select one of the following options:

``Python Fix Imports``

    Fix imports in the current file.

``Enable Python Fix Imports (until restart)``

    Toggle the general settings ``autofix_on_save`` to ``Enabled`` until Sublime restart (overwrite
    the project and global settings).

``Disable Python Fix Imports (until restart)``

    Toggle the general settings ``autofix_on_save`` to ``Disabled`` until Sublime restart (overwrite
    the project and global settings).

``Disable Python Fix Imports for this file (until restart)``

    Disable the automatical fix of the import statements in the current file, independentely of the
    global setting ``autofix_on_save``.

``Enable Python Fix Imports for this file (until restart)``

    Enable the automatical fix of the import statements in the current file, independentely of the
    global setting ``autofix_on_save``.

Hint: open Command Palette (``ctrl+shift+P``) and type ``Fix...`` up to highlight full caption.

License
*******

Copyright 2015 Semet Gaetan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
