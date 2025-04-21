

def get_lists():
    lst = []
    elem = input("Enter the List if you want to stop perss enter")
    
    while (elem != ""):
      lst.append(elem)
      elem = input("Enter the List if you want to stop perss enter")
    return lst

def main():

 lst = get_lists()
 print(lst[0])

if __name__ == "__main__":
    main()
