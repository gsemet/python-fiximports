# -*- coding: utf-8 -*-

# Copyright 2012-2013 Stéphane Bunel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import sublime
import sublime_plugin

PPA_PATH = list()
PYMAMI = '{0}{1}'.format(*sys.version_info[:2])
ST_VERSION = 3000 if sublime.version() == '' else int(sublime.version())
PLUGIN_NAME = "Python Fix Imports"
SETTINGS_FILE = 'python_fiximports.sublime-settings'

#-- Cannot use sublime.packages_path() with ST3 because of inconsistency
#-- of returned path between bootstap time vs running time.
#pkg_path = os.path.join(sublime.packages_path(), PLUGIN_NAME)
pkg_path = os.path.abspath(os.path.dirname(__file__))
libs_path = os.path.join(pkg_path, 'libs')
PPA_PATH.append(libs_path)

versionlibs_path = os.path.join(pkg_path, 'libs', 'py' + PYMAMI)
if os.path.exists(versionlibs_path):
    PPA_PATH.append(versionlibs_path)

print('Python fiximports: included directory to sys.path :', PPA_PATH)
[sys.path.insert(0, p) for p in PPA_PATH if p not in sys.path]

try:
    from . import fiximports
    import MergeUtils
except:
    sublime.error_message(
        '{0}: import error: {1}'.format(PLUGIN_NAME, sys.exc_info()[1]))
    raise


class PythonFiximportsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        syntax = self.view.settings().get('syntax')
        if syntax.lower().find('python') == -1:
            return
        replace_region = self.view.line(
            sublime.Region(0, self.view.size()))
        source = self.view.substr(replace_region)
        # split_import_statements = self.settings.get('split_import_statements', False)

        self.settings = sublime.load_settings(SETTINGS_FILE)

        fixed = fiximports.FixImports().sortImportGroups("filename", source)
        fixed = source
        #is_dirty, err = MergeUtils.merge_code(self.view, edit, source, fixed)
        # if err:
        #     sublime.error_message(
        #         "%s: Merge failure: '%s'" % (PLUGIN_NAME, err))
        #     raise


class PythonFixImportsBackground(sublime_plugin.EventListener):

    def on_pre_save(self, view):
        self.settings = sublime.load_settings(SETTINGS_FILE)

        syntax = view.settings().get('syntax')
        if syntax.lower().find('python') == -1:
            return

        # do autoformat on file save if allowed in settings
        if self.settings.get('autofix_on_save', False):
            view.run_command('python_fiximports')
