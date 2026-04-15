def main():

    try:
        a = int(input("hey enter a number : "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("hey I am inside of finally")

main()          #finally does ont obey return 