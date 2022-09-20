class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = True if self.is_on != True else False

    def install(self, app, app_memory):
        out_put = ''
        if app_memory <= self.memory:
            out_put = f'Installing {app}'
            if not self.is_on:
                out_put = f'Turn on your phone to install {app}'
            else:
                self.apps.append(app)
                self.memory -= app_memory
        else:
            out_put = f'Not enough memory to install {app}'
        return out_put

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
