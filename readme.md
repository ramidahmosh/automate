# pytest with selenium qa automation platform Linux(ubuntu)

##installation :
 - sudo apt install -y python3-pip
 - pip3 install -r requirments.txt


##install allure:
 - unzip allure2.7.zip and copy it to /opt
 - cd /usr/bin
 - sudo ln -s /opt/allure-2.7.0/bin/allure allure


##run test with allure:
 - python3 -m pytest  --alluredir=report test/selenium_test/test_ebay_prices.py
 - allure serve report 
