huruf = input("masukan huruf: ")

vokal = "aiueo"
if not huruf.isalpha():
    print("bukan huruf")
elif huruf.lower() in vokal:
    print(f"huruf {huruf.lower()} merupakan vokal")
else:
    print(f"huruf {huruf.lower()} merupakan konsonan")