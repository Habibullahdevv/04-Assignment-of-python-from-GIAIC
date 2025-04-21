def main():
 

 number: list[int] = [1,2,3,4]

 for i in range(len(number)):
  inti = number[i]
  number[i] = inti*2
 print(number)


if __name__ == '__main__':
 main()