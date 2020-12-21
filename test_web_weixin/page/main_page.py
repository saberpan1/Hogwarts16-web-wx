from test_web_weixin.page.add_member_page import AddMemberPage
from test_web_weixin.page.contact_page import ContactPage
from selenium import webdriver

class MainPage:

    def goto_add_member(self):
        """
        跳转到添加成员
        :return:
        """
        driver = webdriver.Chrome()
        return AddMemberPage()

    def goto_contanct(self):
        """
        跳转到通讯录页面
        :return: 
        """
        return ContactPage()
