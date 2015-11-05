import os, sublime, sublime_plugin
class composerCommand(sublime_plugin.TextCommand):
	def run(self, edit, config = 'update'):
		working_dir = '--working-dir=C:\wamp\www\GIPSI\core';
		os.system("php.exe C:ProgramData\\ComposerSetup\\bin\\composer.phar "+working_dir+" "+config)