import things


class Page(object):
    def __init__(self):
        pass


class Button(object):
    def __init__(self, size, color, link):
        self.size = size
        self.color = color
        self.link = link

mypage = Page()

login_button = Button(
    size = 5,
    color = "purple",
    link = login_link,
)

logout_button = Button(
    color = "red",
    link = logout_link,
)

mypage.buttons.add(login_button, logout_button):
