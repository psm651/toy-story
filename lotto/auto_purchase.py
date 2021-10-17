from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


def auto_purchase(lotto_id, lotto_password):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get('https://dhlottery.co.kr/common.do?method=main')

    windows_list = driver.window_handles
    main_window = driver.window_handles[0]

    # 팝업닫기
    cnt = 1
    for i in range(len(windows_list)-1):
        driver.switch_to.window(windows_list[cnt])
        driver.close()
        cnt += 1

    # 메인창 focus 이동
    driver.switch_to.window(main_window)

    # 로그인버튼
    driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/form/div/ul/li[1]/a').click()

    # 대기
    driver.implicitly_wait(5)

    # 로그인
    driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div[2]/div/form/div/div[1]/fieldset/div[1]/input[1]').send_keys(lotto_id)
    driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/input[2]').send_keys('lotto_password')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a').click()
    driver.implicitly_wait(5)

    windows_list = driver.window_handles
    main_window = windows_list[0]

    # 팝업닫기
    cnt = 1
    for i in range(len(windows_list)-1):
        driver.switch_to.window(windows_list[cnt])
        driver.close()
        cnt += 1

    # 메인창 focus 이동
    driver.switch_to.window(main_window)

    # 복권구매 GNB
    driver.find_element(By.XPATH, '//*[@id="gnb"]/ul/li[1]/a').click()
    # 로또645클릭
    driver.find_element(By.XPATH, '//*[@id="gnb"]/ul/li[1]/div/ul/li[1]/a').click()

    # 새창 focus 이동
    windows_list = driver.window_handles
    new_window = windows_list[1]
    driver.switch_to.window(new_window)

    # iframe 여러개 있을 경우를 대비
    iframes = driver.find_elements(By.CSS_SELECTOR, 'iframe')

    for iframe in iframes:
        print(iframe.get_attribute('id'))

    # iframe 탭 이동
    driver.switch_to.frame('ifrm_tab')
    driver.implicitly_wait(5)

    # 자동선택 클릭
    driver.find_element(By.XPATH, '// *[ @ id = "num2"]').click()
    # 좌측 확인
    driver.find_element(By.XPATH, '//*[@id="btnSelectNum"]').click()
    # 우측 구매하기
    driver.find_element(By.XPATH, '//*[@id="btnBuy"]').click()
    # 구매확정
    driver.find_element(By.XPATH, '// *[ @ id = "popupLayerConfirm"] / div / div[2] / input[1]').click()


if __name__ == '__main__':
    id = '';
    password = '';
    auto_purchase(id,password)

