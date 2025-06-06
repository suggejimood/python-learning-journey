def divide(x, y):
    try: 
        result = x / y
    except ZeroDivisionError:
        print("Sıfıra bölünme hatası")
    else:
        print("Sonuç:", result)
    finally:
        print("İşlem tamamlandı.")

divide(10, 0)
divide(10, 5)
divide(2, 4)

#Özel hata türler: ValueError, TypeError, IndexError, KeyError, AttributeError, ZeroDivisionError, FileNotFoundError, ImportError, AssertionError

