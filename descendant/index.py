class LoggableList(list, Loggable):
    def append(self, msg):
        super(LoggableList, self).append(msg)
        self.log(msg)