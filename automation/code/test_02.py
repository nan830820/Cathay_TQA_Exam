from base import *


class Test_02(CathayBankScreenshotter):
    def capture_credit_card_menu(self, url, filename="cathaybk_credit_card_menu"):
        try:
            self.driver.get(url)
            time.sleep(5)

            personal_finance_button = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[contains(text(), "個人金融")]'))
            )
            time.sleep(2)

            product_intro_button = WebDriverWait(self.driver, self.wait_time).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[contains(text(), "產品介紹")]'))
            )
            product_intro_button.click()
            time.sleep(2)

            credit_card_menu = WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[contains(text(), "產品介紹")]/following::div[contains(text(), "信用卡")][1]'))
            )
            time.sleep(2)

            self.screenshot(filename)
            print(f"信用卡選單截圖完成：{filename}.png")
        except Exception as e:
            print(f"主流程中發生錯誤：{e}")
        finally:
            self.close()


if __name__ == "__main__":
    url = "https://www.cathay-cube.com.tw/cathaybk"
    screenshotter = Test_02()
    screenshotter.capture_credit_card_menu(url)
