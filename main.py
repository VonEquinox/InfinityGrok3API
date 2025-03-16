import time
import random
import undetected_chromedriver as uc  # 导入 undetected_chromedriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip

def Send(question):
    print("sending....")
    pyperclip.copy(question)

    time.sleep(random.uniform(0.2, 0.6))

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.pause(random.uniform(0.2, 0.5))
    actions.key_down('v')
    actions.pause(random.uniform(0.05, 0.1))
    actions.key_up('v')
    actions.pause(random.uniform(0.1, 0.3))
    actions.key_up(Keys.CONTROL)

    actions.pause(random.uniform(0.2, 0.5))
    for i in range(0, 4):
        actions.key_down(Keys.TAB)
        actions.pause(random.uniform(0.05, 0.1))
        actions.key_up(Keys.TAB)
        actions.pause(random.uniform(0.2, 0.5))

    actions.key_down(Keys.ENTER)
    actions.pause(random.uniform(0.05, 0.1))
    actions.key_up(Keys.ENTER)
    actions.perform()

def GetLink():
    print("getting link...")
    actions = ActionChains(driver)
    for i in range(0, 7):
        actions.key_down(Keys.TAB)
        actions.pause(random.uniform(0.05, 0.1))
        actions.key_up(Keys.TAB)
        actions.pause(random.uniform(0.2, 0.5))
    
    actions.key_down(Keys.ENTER)
    actions.pause(random.uniform(0.05, 0.1))
    actions.key_up(Keys.ENTER)
    actions.perform()


def clean_all():
    driver.delete_all_cookies()
    print("已删除所有cookie")
    try:
        driver.execute_script('localStorage.clear();')
        print("Local Storage 清理完成.")
    except Exception as e:
        print(f"清理 Local Storage 失败: {e}")

    # 3. 清理 Session Storage
    print("清理 Session Storage...")
    try:
        driver.execute_script('sessionStorage.clear();')
        print("Session Storage 清理完成.")
    except Exception as e:
        print(f"清理 Session Storage 失败: {e}")

    driver.refresh()
    print("已刷新页面")

if __name__ == "__main__":
    # 1. 获取当前 Chrome 浏览器的 User-Agent (使用 undetected_chromedriver 获取)
    print("正在获取User-Agent")
    temp_options = uc.ChromeOptions()  # 使用 uc.ChromeOptions
    temp_driver = uc.Chrome(options=temp_options, use_subprocess=True) # 开启use_subprocess
    user_agent = temp_driver.execute_script("return navigator.userAgent;")
    temp_driver.quit()
    print(f"获取到 User-Agent: {user_agent}")

    # 2. 配置 ChromeOptions，添加反自动化检测措施
    options = uc.ChromeOptions()  # 使用 uc.ChromeOptions
    options.add_argument(f"user-agent={user_agent}")

    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--mute-audio")

    options.add_experimental_option("prefs", {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.default_content_setting_values.notifications": 2,
    })

    # 3. 初始化 WebDriver (使用 undetected_chromedriver)
    print("正在启动浏览器")
    driver = uc.Chrome(options=options, use_subprocess=True)  # 开启use_subprocess, 避免 chromedriver.exe 闪退
    print("启动浏览器成功")

    # 4. 设置隐式等待 (重要：undetected_chromedriver 可能需要更长的加载时间)
    driver.implicitly_wait(3)  # 设置一个较长的隐式等待时间，例如 30 秒

    driver.get("https://www.grok.com/")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="问格罗克"]')))
    clean_all()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="问格罗克"]')))

    actions = ActionChains(driver)
    actions.pause(random.uniform(0.2, 0.5))

    actions.key_down('1')
    actions.pause(random.uniform(0.05, 0.1))
    actions.key_up('1')
    actions.pause(random.uniform(0.1, 0.3))
    actions.key_down(Keys.BACK_SPACE)
    actions.pause(random.uniform(0.05, 0.1))
    actions.key_up(Keys.BACK_SPACE)
    actions.perform()

    response_list = []
    string_set = set()
    counter = 0
    context = True
    while True:
        question = input("Question:")
        if counter == 3:
            # if context:
            #     GetLink()
            #     time.sleep(1)
            #     print(pyperclip.paste())
            #     driver.get(pyperclip.paste())
            #     time.sleep(3)
            #     for i in range(0, 9):
            #         actions.key_down(Keys.TAB)
            #         actions.pause(random.uniform(0.05, 0.1))
            #         actions.key_up(Keys.TAB)
            #         actions.pause(random.uniform(0.2, 0.5))
            #     actions.key_down(Keys.ENTER)
            #     actions.pause(random.uniform(0.05, 0.1))
            #     actions.key_up(Keys.ENTER)
            #     actions.perform()
            # else:
            #     clean_all()
            clean_all()
            counter = 0
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="DeepSearch"]')))

        Send(question)
        counter += 1
        print("outputing...")

        while True:
            try:
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div > div.flex.items-center.gap-\\[2px\\].w-max.opacity-0.group-focus-within\\:opacity-100.group-hover\\:opacity-100.transition-opacity.rounded-lg.text-xs.bg-background.pb-2.px-2.start-0.md\\:start-3.-ml-4.group-last-of-type\\:opacity-100')#.find_element(By.CLASS_NAME,'flex.items-center.gap-\[2px\]')
                break
            except Exception as e:
                continue

        print("success!")

        try:
            results = driver.find_elements(By.CSS_SELECTOR, 'div.w-full.max-w-3xl.flex.flex-col')
            for result in results:
                response_text = result.find_element(By.CSS_SELECTOR, '[dir="auto"]').text
                if response_text not in string_set:
                    string_set.add(response_text)
                    response_list.append(response_text)
                    print(response_text)
        except Exception as e:
            print(e)