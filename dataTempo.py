'''
%a - Weekday as locale’s abbreviated name.
    Sun, Mon, …, Sat (en_US);
    So, Mo, …, Sa (de_DE)
%A - Weekday as locale’s full name.
    Sunday, Monday, …, Saturday (en_US);
    Sonntag, Montag, …, Samstag (de_DE)
%w - Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
    0, 1, …, 6
%d - Day of the month as a zero-padded decimal number.
    01, 02, …, 31
%b - Month as locale’s abbreviated name.
    Jan, Feb, …, Dec (en_US);
    Jan, Feb, …, Dez (de_DE)
%B - Month as locale’s full name.
    January, February, …, December (en_US);
    Januar, Februar, …, Dezember (de_DE)
%m - Month as a zero-padded decimal number.
    01, 02, …, 12
%y - Year without century as a zero-padded decimal number.
    00, 01, …, 99
%Y - Year with century as a decimal number.
    0001, 0002, …, 2013, 2014, …, 9998, 9999
%H - Hour (24-hour clock) as a zero-padded decimal number.
    00, 01, …, 23
%I - Hour (12-hour clock) as a zero-padded decimal number.
    01, 02, …, 12
%p - Locale’s equivalent of either AM or PM.
    AM, PM (en_US);
    am, pm (de_DE)
%M - Minute as a zero-padded decimal number.
    00, 01, …, 59
%S - Second as a zero-padded decimal number.
    00, 01, …, 59
%f - Microsecond as a decimal number, zero-padded on the left.
    000000, 000001, …, 999999
%z - UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
    (empty), +0000, -0400, +1030, +063415, -030712.345216
%Z - Time zone name (empty string if the object is naive).
    (empty), UTC, GMT
%j - Day of the year as a zero-padded decimal number.
    001, 002, …, 366
%U - Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. 
All days in a new year preceding the first Sunday are considered to be in week 0.
    00, 01, …, 53
%W - Week number of the year (Monday as the first day of the week) as a decimal number. 
All days in a new year preceding the first Monday are considered to be in week 0.
    00, 01, …, 53
%c - Locale’s appropriate date and time representation.
    Tue Aug 16 21:30:00 1988 (en_US);
    Di 16 Aug 21:30:00 1988 (de_DE)
%x - Locale’s appropriate date representation.
    08/16/88 (None);
    08/16/1988 (en_US);
    16.08.1988 (de_DE)
%X - Locale’s appropriate time representation. 21:30:00 (en_US);
%% - A literal '%' character.
'''
from datetime import date, time, datetime
def usandoDate():
    diaHoje = date.today()
    print(diaHoje.strftime('%d/%m/%Y'))
    print(diaHoje.strftime('%a/%B/%Y'))
def usandoTime():
    horario = time(hour=14,minute=20,second=23)
    print(horario)
    print(horario.strftime('%H:%M:%S'))
def usandoDateTime():
    dataAtual = datetime.now()
    print(dataAtual)
    print(dataAtual.strftime('%d-%m-%Y %H:%M:%S'))
    print(dataAtual.day)
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domigo')
    print(tupla[dataAtual.weekday()])
    dataString = '02/04/2019'
    dataNumero = datetime.strptime(dataString,'%d/%m/%Y')
    print(dataNumero)
   
if __name__=='__main__':
    #usandoDate()
    #usandoTime()
    usandoDateTime()