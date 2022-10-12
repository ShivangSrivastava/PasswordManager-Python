import calculator
import firsttimepasswordsaver

if firsttimepasswordsaver.SavePassword().is_password_not_there():
    firsttimepasswordsaver.Window().start()

calculator.Calculator().run()
