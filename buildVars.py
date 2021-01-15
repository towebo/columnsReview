# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "columnsReview",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Columns Review"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""Provides 10+1 gestures to read and copy the list columns header and content"""),
	# version
	"addon_version" : "3.0-20210115-dev",
	# Author(s)
	"addon_author" : u"Alberto Buffolino <a.buffolino@gmail.com>, Łukasz Golonka <lukasz.golonka@mailbox.org>",
	# URL for the add-on documentation support
	"addon_url" : "https://addons.nvda-project.org",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion" : "2017.3",
	# Last NVDA version supported/tested (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2020.4",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : "dev",
}

import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "columnsReview", "*.py"), os.path.join("addon", "installTasks.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
