import requests
from bs4 import BeautifulSoup

def run():
    print("爬虫任务开始执行...")
    url = "https://google.com"
    response = requests.get(url, timeout=10)
    response.encoding = "utf-8"  # 强制转为 UTF-8
    soup = BeautifulSoup(response.text, "lxml")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        title = soup.title.string if soup.title else "未找到标题"
        print("页面标题:", title)
    else:
        print("请求失败，状态码:", response.status_code)
    print("爬虫任务执行完成。")

if __name__ == "__main__":
    run()
