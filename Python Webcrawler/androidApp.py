class androidApp(object):

    def __init__(self,name,link):
        self.name = name
        self.link = link
        appVersions = []
        author = ""
        description = ""
    
    def addVersion(self,versionNumber,downloadLink):
        #create and append version object to the appVersions list
        appVersions.append(androidVersion(versionNumber,downloadLink))

    def setAuthor(self,author):
        self.author = author

    def setDescription(self,description):
        self.description = description
    
    def __str__(self):
        return("name: " + self.name + "\nlink: " + self.link + "\nauthor: " + self.author + "\ndescription: " + self.description)
    
class androidVersion(object):

    def __init__(self,number,link):
        self.number = number
        self.link = link