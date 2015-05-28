import os, sublime, sublime_plugin
class codedeliveryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		fichier_cli = self.view.file_name()
		if (fichier_cli.find("aperam\\") < 0):
			sublime.message_dialog(fichier_cli + ' is not in aperam context')
		else:
			drive       = fichier_cli.split(":", 1)[0]
			gipsi_path  = fichier_cli.split("aperam\\", 1)[0]+"aperam\\cli"
			os.system(drive+": & cd  "+gipsi_path+" & php.exe -c ../php.ini ../wwwroot/page.php --include=batch --page_plugin=CodeDelivery --page=start --config=CodeDelivery")