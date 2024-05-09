def main():
    height=int(input("Enter the height of the pyramid :"))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(" "*(n-1) , end="")
        print("#"*(i+1))
        n-=1
        

main()