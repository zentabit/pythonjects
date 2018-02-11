from selenium import webdriver
from selenium.webdriver.support.ui import Select
from openpyxl import load_workbook
import requests, os


# Fill out the element with name name
def fill(elem_name, value):
    elem = browser.find_element_by_name(elem_name)
    elem.clear()
    elem.send_keys(value)


# Fill out form and download image
def get_image(name, surname, title):
    browser.get("http://photofunia.com/effects/hogwarts_letter")

    print('Selected %s %s, please wait while magic happens...' % (name, surname))

    select = Select(browser.find_element_by_css_selector('.custom-select select'))
    if title == "Mr":
        select.select_by_visible_text("Mr")
    elif title == "Ms":
        select.select_by_visible_text("Ms")
    
    fill('name', name)
    fill('surname', surname)
    fill('address', 'IT-Gymnasiet')
    fill('address2', 'Origovägen 4')
    fill('address3', 'Göteborg')

    elem = browser.find_element_by_class_name('replacement')
    elem.click()

    elem = browser.find_element_by_class_name('js-send-button')
    elem.click()

    elem = browser.find_element_by_class_name('button')
    url = elem.get_attribute('href')

    print("Downloading image %s" % (url))
    res = requests.get(url)

    print('Saving into %s' % (os.path.join('image', ('%s_%s.jpg' % (name, surname)))))
    image_file = open(os.path.join('image', ('%s_%s.jpg' % (name, surname))), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    print()


#Filters through the excel sheet, and creates images
def search_and_image(sheet):
    for row in sheet:  
    # If Cx == "ÄLSKAR DET!!!!!!11!!" and Dx == "9 3/4" then get first and last from Bx and get_image
        if row[2].value == "ÄLSKAR DET!!!!!!11!!" and row[3].value == "9 3/4":
            var = row[1].value.split('.')
            name = var[0]
            name = name[:1].upper() + name[1:]
            surname = var[1].split('@')[0]
            surname = surname[:1].upper() + surname[1:]
            get_image(name, surname, row[4].value)
        

browser = webdriver.Firefox()
wb = load_workbook(os.path.join(os.getcwd(), 'file.xlsx'))
sheet = wb['Formulärsvar 1']

search_and_image(sheet)