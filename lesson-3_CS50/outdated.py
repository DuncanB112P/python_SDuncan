months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
     while True:
          try:
               x= input('Date: ')

               if '/' in x:
                    n = get_numbers(x)
                    day = int(n[1])
                    month = int(n[0])
                    year = int(n[2])
                    if day < 1 or day > 31:
                         continue
                    if month < 1 or month > 12:
                         continue
                    else:
                         print(f"{year:04d}-{month:02d}-{day:02d}")
                         break
               
               if ',' in x:
                    n = get_numbers2(x)
                    day = int(n[1])
                    month = int(n[0])
                    year = int(n[2])
                    date = (f"{year:04d}-{month:02d}-{day:02d}")
                    if day < 1 or day > 31:
                         continue
                    if month < 1 or month > 12:
                         continue
                    else:
                         print(date)
                         break                      
          
          except (UnboundLocalError, ValueError):
               pass
     

def get_numbers(r):
     list = r.split('/')
     return list

def get_numbers2(r):
     list = r.split()
     day = int(list[1].strip(','))
     year = int(list[2])
     month = None
     for i, m in enumerate(months, start = 1):
          if m in r:
               month = i
     return [month, day, year]

     


main()