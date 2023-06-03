try:
    voyazh = {"Мексика", "Канада", "Израиль", "Италия"}
    reinatur = {"Англия", "Япония", "Канада", "ЮАР"}

    print(voyazh - reinatur)
    print(reinatur - voyazh)
    print(voyazh & reinatur)
    print(voyazh == reinatur)
except:
    print('Error')