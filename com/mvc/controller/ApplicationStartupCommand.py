from com.mvc.view.ApplicationMediator import ApplicationMediator
from puremvc.interfaces import INotification
from puremvc.patterns.command import SimpleCommand


class ApplicationStartupCommand(SimpleCommand):
    def execute(self, notification: INotification):
        self.facade.registerMediator(ApplicationMediator(notification.getBody()))
        pass
