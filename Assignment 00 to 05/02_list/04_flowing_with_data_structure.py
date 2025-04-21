def list_three_times(my_list, data):
    for i in range(3):
     my_list.append(data)

def main():
  message = input("Enter a message that you want to print three times: ")
  my_list = []
  print(f"List before {my_list}")
  list_three_times(my_list, message)
  print(f"List after {my_list}")

if __name__ == "__main__":
    main()
