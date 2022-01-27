import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver import ChromeOptions
from chaojiying import Chaojiying_Client
from selenium.webdriver.chrome.options import Options

# 创建浏览器对象
global web
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
web = Chrome(options=option)
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator,'webdriver',{
     get: () => false
    })
    """
})

# 准备无头浏览器配置信息
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')


# 打开网址
def search(start, end):
    web.get("https://wenshu.court.gov.cn/")
    web.maximize_window()
    time.sleep(2)
    web.refresh()

    login_tag = web.find_element(By.XPATH, '//*[@id="loginLi"]/a')
    # 点击登录
    time.sleep(2)
    login_tag.click()
    time.sleep(2)
    web.refresh()

    # 验证码的问题
    # img = web.find_element(By.XPATH, '//*[@id="Image1"]').screenshot_as_png
    # chaojiying = Chaojiying_Client('ukryssh', 'su20030226', '926298')
    # dic = chaojiying.PostPic(img, 1902)
    # verifyCode = dic['pic_str']
    # web.find_element(By.XPATH, '/html/body/div/div/div[4]/form/div[1]/input').send_keys(verifyCode)
    # web.find_element(By.XPATH, '/html/body/div/div/div[4]/form/div[2]/input').click()

    # 输入账号密码登录
    time.sleep(2)
    username_path = web.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div[1]/div/div/div/input')
    password_path = web.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div[2]/div/div/div/input')
    time.sleep(1)
    login_path = web.find_element(By.XPATH, '//*[@id="root"]/div/form/div/div[3]/span')
    time.sleep(1)
    username_path.send_keys("***********")  # 需输入账号
    time.sleep(2)
    password_path.send_keys("***********")  # 需输入密码
    time.sleep(2)
    login_path.click()
    time.sleep(5)

    # 输入日期
    start_date_path = web.find_element(By.XPATH, '//*[@id="cprqStart"]')
    end_date_path = web.find_element(By.XPATH, '//*[@id="cprqEnd"]')
    start_date_path.send_keys(str(start.year)+"-"+str(start.month)+"-"+str(start.day))
    end_date_path.send_keys(str(end.year)+"-"+str(end.month)+"-"+str(end.day))
    search_path = web.find_element(By.XPATH, '//*[@id="searchBtn"]')
    search_path.click()
    # search_path = web.find_element(By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input')
    # search_path.send_keys("南京", Keys.ENTER)
    # time.sleep(2)
    web.refresh()
    time.sleep(10)

    # 爬取100篇判决书 翻动20页一次下载
    try:
        for i in range(0, 7):
            download_path1 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[3]/div[6]/div/a[2]')
            download_path2 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[4]/div[6]/div/a[2]')
            download_path3 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[5]/div[6]/div/a[2]')
            download_path4 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[6]/div[6]/div/a[2]')
            download_path5 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[7]/div[6]/div/a[2]')
            # 下一页bottom的Xpath路径a[i]最多到14
            next_page_path = web.find_element(By.XPATH, f'//*[@id="_view_1545184311000"]/div[8]/a[{i + 8}]')
            download_path1.click()
            time.sleep(1)
            download_path2.click()
            time.sleep(1)
            download_path3.click()
            time.sleep(1)
            download_path4.click()
            time.sleep(1)
            download_path5.click()
            time.sleep(1)
            next_page_path.click()
            time.sleep(3)

        for i in range(0, 15):
            download_path1 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[3]/div[6]/div/a[2]')
            download_path2 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[4]/div[6]/div/a[2]')
            download_path3 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[5]/div[6]/div/a[2]')
            download_path4 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[6]/div[6]/div/a[2]')
            download_path5 = web.find_element(By.XPATH, '//*[@id="_view_1545184311000"]/div[7]/div[6]/div/a[2]')
            next_page_path = web.find_element(By.XPATH, f'//*[@id="_view_1545184311000"]/div[8]/a[14]')
            download_path1.click()
            time.sleep(1)
            download_path2.click()
            time.sleep(1)
            download_path3.click()
            time.sleep(1)
            download_path4.click()
            time.sleep(1)
            download_path5.click()
            time.sleep(1)
            next_page_path.click()
            time.sleep(3)
    except Exception:
        pass

