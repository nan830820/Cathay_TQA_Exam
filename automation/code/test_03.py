from base import *


class Test_03(CathayBankScreenshotter):
    def capture_all_diabled_card_numbers(self, url, filename="cathaybk_credit_card_menu"):
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

            # 點擊卡片介紹元素
            card_intro = WebDriverWait(self.driver, self.wait_time).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//a[@title="前往卡片介紹"]'))
            )
            card_intro.click()
            time.sleep(2)

            # 滾動並定位到停發卡元素
            target_element = WebDriverWait(self.driver, self.wait_time).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="cubre-a-iconTitle__text" and contains(text(), "停發卡")]'))
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", target_element)
            WebDriverWait(self.driver, self.wait_time).until(
                EC.visibility_of(target_element))

            # 定位到停發卡分頁圓點
            pagination_bullets = self.driver.find_elements(
                By.XPATH, '//section[@data-anchor-block="blockname06"]//div[contains(@class, "swiper-pagination-bullets")]/span'
            )

            print(f"共有 {len(pagination_bullets)} 個停發卡。")

            for i, bullet in enumerate(pagination_bullets):
                self.driver.execute_script("arguments[0].click();", bullet)
                time.sleep(1)
                self.screenshot(f'{filename}_{i+1}')

            print(f"信用卡選單截圖完成：{filename}.png")
        except Exception as e:
            print(f"主流程中發生錯誤：{e}")
        finally:
            self.close()


if __name__ == "__main__":
    url = "https://www.cathay-cube.com.tw/cathaybk"
    screenshotter = Test_03()
    screenshotter.capture_all_diabled_card_numbers(url)
