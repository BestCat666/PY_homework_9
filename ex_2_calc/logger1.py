# import datetime
# import main
# def logger_():
#     file = 'logger.txt'
#     now = str(datetime.datetime.now())
#     data = f"{main.res}, {now}"
#     with open('logger.txt', 'a+', encoding='utf-8') as file:
#         file.write(data)



# import main
# from logging.handlers import RotatingFileHandler
# now = datetime.datetime.now()
# level = logging.info
# massge = 'логи выведены'
# logging.basicConfig(
#     level = logging.info
#     filename= 'logger.txt'
#     format='%(now)s, %(level)s, %(name),  %(message)s')
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler = RotatingFileHandler('logger.txt', maxBytes=50000000, backupCount=5)
# logger.addHandler(handler) 
# logging.basicConfig(filename= 'logger.txt', filemode='w') 