class gdrive(Command):
    """
    Uploads the selected files to google drive via gdrive
    """
    def execute(self):
        file = self.fm.thisfile
        self.fm.run("gdrive upload \"{0}\" {1}".format(file.basename, self.rest(1)))
        self.fm.notify('Done!')
