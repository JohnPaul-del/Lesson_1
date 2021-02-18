seconds = int(input("Введите количество секунд: "))

years = seconds // 31536000
month = (seconds % 31104000) // 2592000
day = ((seconds % 31104000) % 2592000) // 86400
hour = (((seconds % 31104000) % 2592000) % 86400) // 3600
_min = ((((seconds % 31104000) % 2592000) % 86400) % 3600) // 60
sec = seconds % 60

print("лет:", years, " месяцев:", month, " дней:", day, " часов:", hour, " минут:", _min, " секунд:", sec, sep="")
