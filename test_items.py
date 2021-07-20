import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element_by_class_name("btn.btn-lg.btn-primary")
    assert button, "there is a button"
