from Views.MainView import MainView
from Models.CurrencyManager import CurrencyManager

class MainApp():
    def __init__(self):
        self.__master = MainView(convert_handler = self.__convert)
        self.__currency = CurrencyManager.get_currency(str(self.__master.currency_name))

    def run(self):
        self.__master.mainloop()

    def __convert(self, from_currency, to_currency, ammount):
        self.__currency = CurrencyManager.get_currency(from_currency)
        if from_currency == to_currency:
            result = ammount
        else:
            result = str(self.__currency.get_convertion(to_currency, ammount))
        self.__master.update_result(result)

if __name__ == "__main__":
    app = MainApp()
    app.run()