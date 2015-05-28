import os, sublime, sublime_plugin
class cliexecutionCommand(sublime_plugin.TextCommand):
    def run(self, edit, config = 'default'):
        fichier_cli=self.view.file_name()
        gipsi_path = fichier_cli.split("cli\\", 1)[0]+"cli"
        phpFile    = fichier_cli.split("cli\\", 1)[1]
        if (config == 'default' or sublime.ok_cancel_dialog('Please confirm ' + config +' execution of '+phpFile)):
	        os.system("cd  "+gipsi_path+" & start cmd /k php.exe -c ../php.ini "+phpFile+" --email=0 --config="+config)

