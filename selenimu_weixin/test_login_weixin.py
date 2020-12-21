import time

from selenium import webdriver
import pytest

class TestWXlogin:

    def test_demo(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        wb = webdriver.Chrome(options=opt)
        wb.get("https://work.weixin.qq.com/wework_admin/frame")
        print(wb.get_cookies())
        self.getcookie = wb.get_cookies()
    def get_QRcode(self):
        pass

    def test_cookie(self):
        wb = webdriver.Chrome()
        wb.maximize_window()
        wb.implicitly_wait(5)
        wb.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '06X5YKnf5eVG_EEbjp16846H7en_r9XHgCdikCG-dQkMueNSKdNnKoCxK30r944sAadPGSTDR3YoxQQu74C0uIMex1m7_gZgMQrpBJ9jdI3A0aMMK-xzBH9AFhTuayWVtfPR8GjaaP-93kWcaHTZsGQvvje7a8rVn92h1_7jdOmbFwClVyao9Hn50ulRWdrYznIRkK9f3J3t8CwHDw_dfOUmwo52rDcKMrugBEBSdVElb8F5mYsYr7pqMlecORo8Kvyi1eLscexWioARX5H3Ug'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2145342'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850433898219'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850433898219'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325058208248'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'MHmwDlCtis_MShgNrofXU5KMnurge5L8EnRn-WYQGU55vaTS96r3-wiRvWdQOsBU'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s4817205788'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608529517'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '29945910342457648'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608545650, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1ja2v7r'}, {'domain': '.qq.com', 'expiry': 1608616566, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.626427052.1608445228'}, {'domain': '.qq.com', 'expiry': 1923371583, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_66c8cc6df2522'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '7d7379a10e5a9aece1ed4c721da8842b02c0f11c24bc6a2427cd70cd37fd3d29'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640065517, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1607499090,1608445227,1608515463,1608518458'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1105317570'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'WOrtT0tWOS'}, {'domain': '.qq.com', 'expiry': 1671602166, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.904785417.1607499091'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639035079, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1608530176, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '8217943040'}, {'domain': '.work.weixin.qq.com', 'expiry': 1611122175, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies :
            wb.add_cookie(cookie)
        wb.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(2)
        wb.quit()