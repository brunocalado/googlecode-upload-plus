# Description #

This script give some extra functionalities to googlecode-upload.py from [Google Project Host Support](http://code.google.com/p/support/) ([code.google.com/p/support](http://code.google.com/p/support/)).

Executing this in your googlecode project directory will:
  * Get project name, username and password from your .hg/hgrc file
  * Commit
  * Push
  * Create a package (.tar, .tar.7z, tar.gz, tar.bz2) with the files of your project naming it with the version (based on changeset)
  * Send the package to the Downloads page of your project

# Requirements #
  * Python3
  * Mercurial
  * Googlecode project initialized with mercurial repository

# Instructions #
  * Download the last script version ([googlecode\_upload.py](http://code.google.com/p/googlecode-upload-plus/downloads/list)) na guia [Downloads](http://code.google.com/p/googlecode-upload-plus/downloads/list)
  * Copy it to your project directory
  * Execute

