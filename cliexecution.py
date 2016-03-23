import os, sublime, sublime_plugin
class cliexecutionCommand(sublime_plugin.TextCommand):
	def run(self, edit, config = 'default'):
		fichier_cli = self.view.file_name()
		if (fichier_cli.find("cli\\") < 0):
			sublime.message_dialog(fichier_cli + ' is not a cli')
		elif (config == 'default' or sublime.ok_cancel_dialog('Please confirm ' + config +' execution of '+fichier_cli)):
			drive       = fichier_cli.split(":", 1)[0]
			cliBat      = fichier_cli.split("cli\\", 1)[0]+"batch"
			phpFile     = fichier_cli.split("cli\\", 1)[1]
			os.system(drive+": & cd "+cliBat+ "& start cli.bat ..\\cli\\"+phpFile+" "+config)