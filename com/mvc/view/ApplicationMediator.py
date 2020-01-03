from com.mvc.notice.NoticeApp import NoticeApp
from puremvc.interfaces import INotification
from puremvc.patterns.mediator import Mediator


class ApplicationMediator(Mediator):
    NAME = "ApplicationMediator"

    def __init__(self, viewComponent):
        super(ApplicationMediator, self).__init__(self.NAME, viewComponent)

    def listNotificationInterests(self):
        return [
            NoticeApp.TEST_EVENT
        ]

    def handleNotification(self, notification: INotification):
        data = notification.getBody()

        if notification.getName() is NoticeApp.TEST_EVENT:
            print("init mvc test")
