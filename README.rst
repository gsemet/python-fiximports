
##################
Python Fix Imports
##################

Python Fix Imports is a Sublime Text 3 plugin ...

History
*******

...

Installation
************

To avoid dependencies, all necessary modules are included within the package.


1. Using [Sublime Package Control][]
    + Use `cmd+shift+P` shortcut then `Package Control: Install Package`
    + Look for `Python Fix Imports` and install it.


1. Using mercurial (hg) repository on bitbucket:
    + Open a terminal, move to Packages directory (refers to the folder that opens when you use the Preferences > Browse Packages… menu). Then type in terminal:
    + `hg clone https://bitbucket.org/StephaneBunel/pythonpep8autoformat 'Python Fix Imports'`


1. Manually:
    + Download an [archive][TagArchive]
      of Python Fix Imports
    + Open a terminal, move to Packages directory (refers to the folder that opens when you use the Preferences > Browse Packages… menu) and create a new directory named 'Python Fix Imports'
    + Extract archive contents in new 'Python Fix Imports' directory.

Settings
********

You'll find settings in Preferences menu (``Preferences -> Package Settings -> Python Fix Imports``).

::

    {
        // Fix the imports on save
        "autofix_on_save": false,

        "split_import_statements": true,
    }

Per-project settings
********************

::

    {
        "settings": {
            "python_fiximports": {
                "autofix_on_save": true
            }
        }
    }

By editing User settings, your personal liking will be kept safe over plugin upgrades.

Usage
*****

Formatting is applied on the whole document.

### Using keyboard:

- GNU/Linux: `ctrl+shift+i`
- OSX:       `ctrl+shift+i`
- Windows:   `ctrl+shift+i`

Using Command Palette:
**********************

You can format your Python code by opening Command Palette (ctrl+shift+P) and type "fix"... up to
highlight full caption.

License
*******

Copyright 2015 Semet Gaetan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
