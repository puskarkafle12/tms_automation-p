from logging import exception
from selenium import webdriver
import datetime, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#stock name lekne hora
stock_name='jblb' 
url="https://tms35.nepsetms.com.np/tms/me/memberclientorderentry"
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# to maximize the browser window
driver.maximize_window()
def check_radio_button_isclicked():
    # print('pkpk '+buy_radio_button.get_attribute('class'))
    if(buy_radio_button.get_attribute('class')=='xtoggler-btn-wrapper is-active'):
        print('buy radio button already clicked')
    if(buy_radio_button.get_attribute('class')=='xtoggler-btn-wrapper'):
        buy_radio_button.click()
        print('buy radio button is not clicked and now it is clicked ')
#order function
def order():
    global high_price
    global previous_high
    global previous_ltp
    global ltp_price



    if symbol_input_box.get_attribute('value')=='ULI':

        # dropdown_element.click() yesma click garnu pardaina drop down confirm garna matrai ho
        qty.send_keys("10")
        # driver.find_element_by_xpath('').send_keys("")
        
        driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input').send_keys(str(high_price))
        # driver.execute_script('document.getElementsByClassName("btn btn-sm ng-star-inserted")[0].removeAttribute("disabled");')
        print('the buy button clicked at: '+(tms_time.text).split()[3]+'\n')
        # check_radio_button_isclicked()

        order_button.click()
        previous_high=high_price
        previous_ltp=ltp_price
        print('previous high',previous_high,'previous ltp',previous_ltp,'current high',high_price,'previous_ltp',previous_ltp)

    else:
        symbol_input_box.clear()
        symbol_input_box.send_keys(stock_name)
        high_price=previous_high
        ltp_price=previous_ltp
        print(stock_name+' '+ symbol_input_box.get_attribute('value') + 'stock name is not matching')
        print('previous high',previous_high,'previous ltp',previous_ltp,'current high',high_price,'previous_ltp',previous_ltp)
#get method to launch the URL
# MN336760
# Puskar123@@@
# 2020094191
# KAFLESP1@
# dummy login
# username='MN336760'
# password='Puskar123@@@'
# driver.get("https://tms35.nepsetms.com.np/login")

username='2020125466'
password='Sunita123@@@'
driver.get("https://tms49.nepsetms.com.np/login")




driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/form/div[1]/input').send_keys(username) #user name
driver.find_element_by_xpath('//*[@id="password-field"]').send_keys(password)  #password

# ###puskar login sys
# driver.get("https://tms35.nepsetms.com.np/login")
# driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/form/div[1]/input').send_keys("PK479690") #user name
# driver.find_element_by_xpath('//*[@id="password-field"]').send_keys("Puskar123@@@")  #password
# # wait until captcha come
# captcha aafile halne 

# driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/form/div[4]/input').click()#click login button


# wait until order management button appears

order_management_button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/tms/app-menubar/aside/nav/ul/li[10]/a/span/span'))
)
# element.click()


#click order management button
order_management_button.click()
#click buy and sell button


buysell_button=driver.find_element_by_xpath('/html/body/app-root/tms/app-menubar/aside/nav/ul/li[10]/ul/li[1]/a')
try:
    buysell_button.click()
except:
    # print('buy button is not interactable exception raised and javascript is executed')
    # driver.execute_script("arguments[0].click();", order_management_button)
    time.sleep(4)
    order_management_button.click()
    buysell_button.click()



#wait until input text box appears stock name halne thau load nahunn jhel samma 
symbol_input_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input'))#dropdown container lai wait garxa
)

symbol_input_box.click()

try:
    
  driver.find_element_by_class_name('box-order-entry box-indeterminate')
except:
    try:
        driver.execute_script('try {document.getElementsByClassName("box-order-entry blur__options box-buy")[0].removeAttribute("class");} catch(err) { document.getElementsByClassName("box-order-entry blur__options box-indeterminate")[0].removeAttribute("class");}')
    except Exception :
        print(Exception())

symbol_input_box.send_keys(stock_name)
# wait until drop down appears
dropdown_wait=WebDriverWait(driver,10)#10 bhaneko maximum wait time 10 sec ho
dropdown_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/typeahead-container'))#dropdown container lai wait garxa
)
# dropdown_element.click() yesma click garnu pardaina drop down confirm garna matrai ho
symbol_input_box.send_keys(Keys.RETURN)#pressing enter button 
buy_radio_button=driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[1]/div[2]/app-three-state-toggle/div/div/label[3]')

buy_radio_button.click()#click buy radio

time.sleep(1)

qty=driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[3]/input')
qty.send_keys("10")

# driver.find_element_by_xpath('').send_keys("")
high_price=driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[3]/b').text
high_price = float(high_price.replace(',', ''))
low_price=float(driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b').text)
ltp_price=driver.find_element_by_xpath("//div[@class='order__form--prodtype price-display ng-star-inserted'][1]").text
ltp_price = ltp_price.split()[1]
print("ltp price ",ltp_price," high price ",high_price," low price",low_price)
ltp_price = float(ltp_price.replace(',', ''))
tms_time=driver.find_element_by_xpath("/html/body/app-root/tms/app-menubar/aside/div[2]/div[1]/span")
driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input').send_keys(str(high_price))
driver.execute_script('document.getElementsByClassName("btn btn-sm ng-star-inserted")[0].removeAttribute("disabled");')


# waiting 
tmstime=(tms_time.text).split()[3]
today = datetime.datetime.strptime(tmstime,"%H:%M:%S")
sleep = (datetime.datetime(today.year, today.month, today.day, 10,59,58) - today).seconds
if sleep<600:
    print('Waiting for ' + str(datetime.timedelta(seconds=sleep)))
    time.sleep(sleep)
else:
    print('runs without waiting')

#buy button clicked

order_button=driver.find_element_by_xpath("//button[@class='btn btn-sm ng-star-inserted btn-primary']")
order_button.click()#class="btn btn-sm ng-star-inserted btn-primary"
#print tms time
time.sleep(3)#sleep 5 sec
print('the buy button clicked at: '+(tms_time.text).split()[3]+'\n')
# check_radio_button_isclicked()
# //button[@class='btn btn-sm ng-star-inserted']


# driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input').send_keys(Keys.RETURN)#pressing enter button 

            

            

def reload():
    try:
        global ltp_price
        global high_price
        global previous_high
        global previous_ltp
        global low_price
        previous_ltp=float(ltp_price)
        previous_high=float(high_price)
        a=1
        symbol_input_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input'))#dropdown container lai wait garxa
    )
        symbol_input_box.send_keys(stock_name)
        while a==1:
        # previous_ltp >= int(ltp_price):
            # if symbol_input_box.get_attribute('value')!=stock_name:
                    
                
            # else:
            # check_radio_button_isclicked()
            # symbol_input_box.send_keys(Keys.BACKSPACE)
            symbol_input_box.clear()
            symbol_input_box.clear()
            symbol_input_box.send_keys(stock_name)
            # wait until drop down appears
            dropdown_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/typeahead-container'))#dropdown container lai wait garxa
            )
            # dropdown_element.click() yesma click garnu pardaina drop down confirm garna matrai ho
            symbol_input_box.send_keys(Keys.RETURN)

        
            high_price=driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[3]/b').text
            high_price = float(high_price.replace(',', ''))
            tms_time=driver.find_element_by_xpath("/html/body/app-root/tms/app-menubar/aside/div[2]/div[1]/span")
            print("ltp price ",ltp_price," high price ",high_price," low price",low_price)
            print('tms_time: '+(tms_time.text).split()[3]+'\n')

            if previous_high<float(high_price):
                    order()
                    low_price=driver.find_element_by_xpath('/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[1]/div[2]/b').text
                    ltp_price=driver.find_element_by_xpath("//div[@class='order__form--prodtype price-display ng-star-inserted'][1]").text
                    ltp_price = ltp_price.split()[1]
                    ltp_price = float(ltp_price.replace(',', ''))
                    print("ltp price ",ltp_price," high price ",high_price," low price",low_price)


    except Exception as e :
        print(e)
        driver.refresh()
        reload()
reload()
    # #waiting 

    # tmstime=tms_time.text
    # today = datetime.datetime.strptime(tmstime,"%H:%M:%S")
    # sleep = (datetime.datetime(today.year, today.month, today.day, 21,52,58) - today).seconds
    # print('Waiting for ' + str(datetime.timedelta(seconds=sleep)))
    # time.sleep(sleep)
    # driver.execute_script('document.getElementsByClassName("btn btn-sm ng-star-inserted")[0]").removeAttribute("disable");')
    # driver.find_element_by_xpath("//button[@class='btn btn-sm ng-star-inserted']").click()
    #to close the browser

    # document.querySelector("body > app-root > tms > main > div > div > app-member-client-order-entry > div > div > div:nth-child(3) > form > div.d-flex.flex-wrap.flex-lg-nowrap.row.mt-3 > div.order__form--btngrp.ml-auto > button.btn.btn-sm.ng-star-inserted.btn-primary").click()
    #element.removeAttribute("disabled");

    # box blur walal
    #element.removeAttribute("_ngcontent-nsd-c11");
    # document.querySelector("body > app-root > tms > main > div > div > app-member-client-order-entry > div > div > div.box-order-entry.blur__options.box-buy")
    # document.getElementsByClassName('box-order-entry blur__options box-buy')[0]
    # implicit wait
    # driver.execute_script('document.getElementsByClassName("btn btn-sm ng-star-inserted")[0]").removeAttribute("disabled");')

    # driver.implicitly_wait(time_to_wait)


    #explict wait
    # wait=WebDriverWait(driver,10)
    # buy_sell_button=wait.until(EC.element_to_be_clickable(By.XPATH,''))
    # buy_sell_button.click()
