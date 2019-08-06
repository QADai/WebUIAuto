## Brief ##
Using Selenium + pytest + Excel Data driver provider for webUI automation testing.

#### folder info ####
- configure: the python class, collect global vars using
- logs: save log file with time stamp
- report: generate resport by allure with pytest result;
- result: get the result by pytest
- screenshot: when test case run failed, will save screenshot here
- testdata: use Excel file for test data
- tools: the different driver file ande the third party scripts

#### code info ####
- base: Encapsulation most of selenium api
- pages: use pages object for testing, define each test page define one class
- testset: test scenoarios sets
- utils:log, read excel capture screenshot, e.g.

#### MORE ####,
base one specific project need do more
Exception;
more detail assertion;
Others;

#### need install module ####

-  selenium  3.141.0
-  xlrd  1.2.0
-  xlwt  1.3.0
-  requests  2.22.0
-  pywin32  224
-  pytest                 5.0.1
-  pytest-allure-adaptor2 1.7.11
-  pytest-metadata        1.8.0
-  pytest-rerunfailures 4.2
