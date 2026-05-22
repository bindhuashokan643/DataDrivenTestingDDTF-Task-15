import os
from datetime import datetime

def take_screenshot(driver, testid):
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = f"{folder}/{testid}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(filename)
    return filename
