# finally override the 'return' function allowing code inside it in any condition of try-exception.
def main():
    try:
        num=int(input("Enter a number: "))
        print (f"You entered {num}.")
        return
    except Exception as e:
        print("you entered string. Please Enter number!")
        return
    finally:
        print("im inside finally.")
if __name__=="__main__":
    main()
    print(__name__)