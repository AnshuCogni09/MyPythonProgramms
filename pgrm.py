def main():
    #fill your code here
    employee = int(input("Enter number of employees: "))

    if employee <= 0:
        print("Invalid input")
        return

    out_dict = {}

    for i in range(1,employee+1):
        name = input("Enter employee name: ")
        products = int(input("Enter number of products sold: "))
        city = input("Enter city: ")
        in_dict = {'name':name, 'products':products}

        if city in out_dict:
            out_dict[city].append(in_dict)
        else:
            out_dict[city] = [in_dict]
       

    print( out_dict)


if __name__=='__main__':
    main()