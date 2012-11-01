import sublime, sublime_plugin

class DuplicateLineCommand(sublime_plugin.TextCommand):
    def run(self, edit,down = True):
		for region in self.view.sel():
			line = self.view.full_line(region)
			self.view.insert(edit, line.begin() if down else line.end(), self.view.substr(line))
		
            
