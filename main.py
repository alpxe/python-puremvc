from com.mvc.controller.ApplicationFacade import ApplicationFacade
from com.mvc.controller.NoticeApp import NoticeApp


class Main:
    def __init__(self):
        print("init Main Class")

        ApplicationFacade.getInstance(ApplicationFacade.NAME).startup(self)

        ApplicationFacade.getInstance(ApplicationFacade.NAME).sendNotification(NoticeApp.TEST_EVENT)
        pass


if __name__ == "__main__":
    Main()
