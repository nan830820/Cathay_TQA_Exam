from base import *


class Test_01(CathayBankScreenshotter):
    def capture_homepage(self, url, filename="cathaybk_homepage"):
        try:
            self.driver.get(url)
            time.sleep(5)
            self.screenshot(filename)
            print(f"截圖完成：{filename}")
        except Exception as e:
            print(f"錯誤發生：{e}")
        finally:
            self.close()


if __name__ == "__main__":
    url = "https://www.cathay-cube.com.tw/cathaybk"
    screenshotter = Test_01()
    screenshotter.capture_homepage(url)
