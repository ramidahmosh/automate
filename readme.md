# pytest with selenium qa automation platform Linux(ubuntu 20.04)

### installation :
 - sudo apt install -y python3-pip
 - pip3 install -r requirments.txt


### install allure:
 - unzip allure2.7.zip and copy it to /opt
 - cd /usr/bin
 - sudo ln -s /opt/allure-2.7.0/bin/allure allure


### under folder werbdriver_drivers there is the broswers drivers


### run normal test:
 - python3 -m pytest test/step_defs/misc/test_ebay_prices.py
 

### run test with allure ( pytest report):
 - python3 -m pytest  --alluredir=report test/step_defs/misc/test_ebay_prices.py
 - allure serve report 


### run repeated test with different input:
 - python3 -m pytest  test/step_defs/parametrize_test/test_plus.py



 