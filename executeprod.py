import os, sublime_plugin
class executeprodCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        fichier_cli=self.view.file_name()
        gipsi_path = fichier_cli.split("cli\\", 1)[0]+"cli"
        phpFile    = fichier_cli.split("cli\\", 1)[1]
        os.system("cd  "+gipsi_path+" & start cmd /k php.exe -c ../php.ini "+phpFile+" --email=0 --config=PROD")
