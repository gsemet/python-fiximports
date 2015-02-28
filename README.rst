##################
Python Fix Imports
##################

Python Fix Imports is a Sublime Text 3 plugin that can automatically reorganize your import
statements. Please read the "Rationals" section for more information.

This plugin comes from a script that has been written for the Buildbot project, in order to help
developers ensuring they properly organize their import statements in there Python files


Rationals
*********

The beginning of the file of each Python script is one the part of the code that is likely to evolve
the most over the lifetime of the code. Imports statements gets added, removed, reorganized all over
the time.

Thanks to distributed versioning systems such as Git, several persons can easily work on the same
time on the same file. And one source of conflict is the management of the ``import`` statements,
that each developers adds his modifications differently.

We really started having the need for automatic reorganization when we have set up an automatic
merge of several branches alltogether. Most of the time, the conflicts were found to be on the
``import`` lines...

Here the organization this ``fiximports`` script enforces:

Rule 1
------

Each import statement only import one object, class or module.

Yes::

    from abc import dce
    from abc import fgh

No::

    from abc import dce, fgh

``fiximports`` automatically splits ``import`` statements that uses a comma. ``\`` and parenthesis
are not supported

*Bonus*: enforcing this rule ensure you can always find occurences of the following search pattern:
``import name_of_the_object``.

Rule 2
------

Import statements are organized in block, separated by an empty line. Each block are alphabetically
sorted.

Yes::

    from abc import aaaa
    from abc import bbbb

No::

    from abc import bbbb
    from abc import aaaa
    from abc import cccc

Sorting only occurs for a given block, if for any reason a given import statement needs to be placed
after another one, just add an empty line.

``fiximports`` can sorts all ``import`` statements at once (preserving the 'group' splitting).


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

        git clone https://github.com/Stibbons/python-fiximports python_fiximports

Settings
********

Global Settings
---------------

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
--------------------

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
---------------

- GNU/Linux: ``ctrl+shift+i``
- OSX:       ``ctrl+shift+i``
- Windows:   ``ctrl+shift+i``

SideBar
-------

Right click on the file(s) or folder(s)

On Save
-------

Imports are reorganized automatically on save if the following setting is set: ``autofix_on_save``.

Command Palette
---------------

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

    Disable the automatic fix of the import statements in the current file, independently of the
    global setting ``autofix_on_save``.

``Enable Python Fix Imports for this file (until restart)``

    Enable the automatic fix of the import statements in the current file, independently of the
    global setting ``autofix_on_save``.

Hint: open Command Palette (``ctrl+shift+P``) and type ``Fix...`` up to highlight full caption.

License
*******

Copyright 2015 Semet Gaetan <gaetan@xeberon.net>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
