import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from androidApp import androidApp

def clickLoadMoreButton():
    try:
        while(True):
            loadMoreButton = driver.find_element_by_class_name("loadmore")
            driver.execute_script("arguments[0].click();", loadMoreButton)
    except:
        return

def getBeautifulSoupWebsiteSource(link):
    req = requests.get(link)
    webpageContent = req.content
    return BeautifulSoup(webpageContent, "html.parser")

def setAuthorAndDescription(app,appPage):
    appAuthor = appPage.find("ul", {"class":"version-ul"}).find("li").find("a").get_text()
    app.setAuthor(appAuthor)
    appDescription = appPage.find("div", {"class":"description"}).get_text()
    app.setDescription(appDescription)
    print(app)

def addAppVersions(appVersionList,app):
    for appVersion in appVersionList:
        print(appVersion['title'] + "\n" + appVersion['href'])

driver = webdriver.Chrome()
antiForensicsKeywords = ["vpn"]
androidAppList = []

#for all the keywords in the anti-forensics keywords list, it will go through the apkpure.com
#website to scrape all the information from every anti-forensics app it can find
for keyword in antiForensicsKeywords:
    #request string for a query on apkpure.com searching with a keyword
    requestString = "https://apkpure.com/search?q=" + keyword
    driver.get(requestString)

    clickLoadMoreButton()

    #get source code from driver then create a beautiful soup object to
    #parse through and search the html
    page = driver.page_source
    soup = BeautifulSoup(page,"html.parser")
    #the html of the div block that contains all the apps inside of it
    appContainer = soup.find("div", {"id":"search-res"})

    #list that will contain each of the a tags for all the apps on the page
    appATags = []
    #list containing all the dt tags for each of the apps shown on the page
    appsInContainer = appContainer.findAll("dt")
    #go through all the apps in the list and add each app's a tag to the appATags list
    for app in appsInContainer:
        appATags.append(app.find("a", href=True, title=True))

    for aTag in appATags:
        #create androidApp object
        appLink = "https://apkpure.com" + aTag['href']
        currentAndroidApp = androidApp(aTag['title'], appLink)
        #get html code of current app's page
        appPage = getBeautifulSoupWebsiteSource(appLink)
        #add author and description information to the androidApp object
        setAuthorAndDescription(currentAndroidApp,appPage)
        #get all the a tags that contain all the versions for that app
        allAppVersions = appPage.find("div", {"id":"faq_box"}).findAll("a", {"class": " down"}, href=True, title=True)
        #add each app version to the app version list in the object
        addAppVersions(allAppVersions,currentAndroidApp)