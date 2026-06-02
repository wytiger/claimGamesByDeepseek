# claim_free_games_github.py
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def setup_driver():
    """配置无头浏览器"""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def claim_steam(driver, username, password):
    """领取Steam免费游戏"""
    print("开始领取Steam免费游戏...")
    try:
        driver.get("https://store.steampowered.com/login/")
        time.sleep(3)
        
        # 登录逻辑（同之前的脚本）
        # ...
        
        print("Steam领取完成")
    except Exception as e:
        print(f"Steam失败: {e}")

def claim_epic(driver, username, password):
    """领取Epic免费游戏"""
    print("开始领取Epic免费游戏...")
    try:
        driver.get("https://store.epicgames.com/zh-CN/free-games")
        time.sleep(5)
        
        # 领取逻辑（同之前的脚本）
        # ...
        
        print("Epic领取完成")
    except Exception as e:
        print(f"Epic失败: {e}")

if __name__ == "__main__":
    # 从环境变量读取账号密码
    steam_user = os.environ.get("STEAM_USERNAME")
    steam_pass = os.environ.get("STEAM_PASSWORD")
    epic_user = os.environ.get("EPIC_USERNAME")
    epic_pass = os.environ.get("EPIC_PASSWORD")
    
    driver = setup_driver()
    try:
        if steam_user and steam_pass:
            claim_steam(driver, steam_user, steam_pass)
        if epic_user and epic_pass:
            claim_epic(driver, epic_user, epic_pass)
    finally:
        driver.quit()
