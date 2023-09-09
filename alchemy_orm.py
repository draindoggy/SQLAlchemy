from sqlalchemy import create_engine, Integer, Column, Text
from sqlalchemy.orm import declarative_base, Session #импорт необходимых зависимостей и библиотек
#create_engine отвечает за подключение к базе, Integer, Text - типы данных sql, Column - колонка соответственно
#declarative_base отвечает за создание таблицы в базе данных, Session - создание сессии


engine = create_engine('postgresql+psycopg2://имя пользователя (обычно - postgres):ваш пароль@адрес хоста/название базы') #подключение к базе данных
session = Session(bind=engine) #создание сессии
Base = declarative_base() #декларирование базы

class tttable(Base): #создание класса (нашей таблицы)
    __tablename__ = 'tttable' #название таблицы
    idd = Column(Integer(), primary_key=True) #название колонки с указанием типа данных
    name = Column(Text)
    surname = Column(Text)
    age = Column(Text)
    city = Column(Text)

c3 = tttable( #переменная, отвечающая за добавление данных в базу
    idd='3',
    name='Maxim',
    surname='Alexandrov',
    age='25',
    city='Kaliningrad'
)

c4 = tttable( #переменная, отвечающая за добавление данных в базу
    idd='4',
    name='John',
    surname='Malkovich',
    age='30',
    city='Los-Angeles'
)
Base.metadata.create_all(engine) #создание таблицы на основе класса и подключения к базе
session.add_all([c3,c4]) #добавление данных в созданную таблицу
s = session.query(tttable.idd, tttable.name, tttable.surname, tttable.age, tttable.city).all() #запрос на выборку данных из таблицы
print(s) #это понятно
session.commit() #подтверждение сессии