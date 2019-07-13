import time
from selenium import webdriver
from selenium.webdriver import ActionChains

address = "https://www.gamee.com/game-bot/" \
          "neonblaster-4c79f24bab9cc49cbef5742d658a5880a2866ea7" \
          "#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DREPbj9XEbOFM7onHYymeSqxGDyOvKK2yQkHvrX_GheE"


driver = webdriver.Firefox()
driver.get(address)
print("get done")
# size = driver.get_window_size()
# print(size)
# width = size['width']
driver.implicitly_wait(5)


driver.find_element_by_class_name("game-controls__button--primary").click()

frame = driver.find_elements_by_tag_name("iframe")[1]

print("frame done")

mouse = ActionChains(driver)

count = 1000
print("entering loop")
for i in range(count):
    print("is in", i)
    movement = ((-1) ** i) * 200
    mouse.click_and_hold(frame)
    mouse.drag_and_drop_by_offset(frame, movement, 0)
    mouse.click_and_hold(frame)


    mouse.perform()
    # driver.get_screenshot_as_png()
