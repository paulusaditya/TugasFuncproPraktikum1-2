
# Tugas 1
#Kode 1
sequenceGenerator = lambda start, stop: list(range(start, stop + 1))
soal = sequenceGenerator(1, 10)
print(soal)

#Soal 2
fizz_buzz_lambda = lambda num: "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else ("Fizz" if num % 3 == 0 else ("Buzz" if num % 5 == 0 else num))
a, b = 10, 30
angka = list(map(fizz_buzz_lambda, range(a, b)))
print(angka)

#Soal 3
def twoNumber(l):
    return list(map(lambda i: l[i] + l[i + 1], range(len(l) - 1)))
soal = twoNumber([1, 2, 3, 4, 5])
print(soal)

