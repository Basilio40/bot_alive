"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""


from botcity.web import WebBot, Browser
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(WebBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Configure whether or not to run on headless mode
        self.headless = False

        self.browse("https://www.acqualivers.com/igortraba")


        
        if not self.find( "selecionar_pais", matching=0.97, waiting_time=18000):
            self.not_found("selecionar_pais")
        self.click()
        self.page_down(wait=0)
        self.click()
        
        if not self.find( "language", matching=0.97, waiting_time=18000):
            self.not_found("language")
        self.click()
        self.page_down(wait=0)
        self.click()
        
        if not self.find( "submit", matching=0.97, waiting_time=18000):
                self.not_found("submit")
        self.click()
        
        
        if not self.find( "afiliar", matching=0.97, waiting_time=18000):
            self.not_found("afiliar")
        self.click()
        
        
        if not self.find( "menino_1", matching=0.97, waiting_time=18000):
            self.not_found("menino_1")
        self.click()
        self.tab(wait=0)
        self.enter()
        
        if not self.find( "afiliar_1", matching=0.97, waiting_time=18000):
            self.not_found("afiliar_1")
        self.click()
        
        if not self.find( "adicionar", matching=0.97, waiting_time=18000):
            self.not_found("adicionar")
        self.click()
        
        if not self.find( "continuar", matching=0.97, waiting_time=18000):
            self.not_found("continuar")
        self.click()

 
        
        # if not self.find( "comecar_1", matching=0.97, waiting_time=1000):
        #     self.not_found("comecar_1")
        # self.click()

        

        


        # Wait for 10 seconds before closing
        self.wait(100000)

        # Stop the browser and clean up
        # self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    try:
        Bot.main()
    except:
        exit(-1)
