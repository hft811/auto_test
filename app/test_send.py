from appium import webdriver


class TestSend:

    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'Android'
        desire_caps['deviceName'] = '127.0.0.1:7555'
        desire_caps['appPackage'] = 'com.tencent.wework'
        desire_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        desire_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_send(self):
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gq_")
        el2.click()
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/ffq")
        el3.click()
        el3.send_keys("今天")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/czs")
        el4.click()
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/dtv")
        el5.click()
        el5.send_keys("测试")
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/dtr")
        el6.click()
        print('测试完成')