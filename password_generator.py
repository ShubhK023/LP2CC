import random
import string

def password_generator(min_lenth,numbers=True,special_characters=True):
    
    letters=string.ascii_letters
    num=string.digits
    special_char=string.punctuation

    characters= letters
    if numbers:
        characters+=num
    if special_characters:
        characters+=special_char

    pwd=""
    has_number=False
    has_specialchar=False
    meets_condition=False 

    while not meets_condition or len(pwd)<min_lenth:
        new_char=random.choice(characters) 
        pwd+=new_char

        if new_char in num:
            has_number=True
        if new_char in special_char:
            has_specialchar=True

        meets_condition=True
        if has_number:
            meets_condition=has_number
        if has_specialchar:
            meets_condition=meets_condition and has_specialchar

    return pwd   
  
def main():
    min_length=int(input("Enter the length of the password: "))
    number=input("Does the password have any numbers?: y/n ").lower()=="y"
    special_char=input("Does the password have any special characters?: y/n ").lower()=="y"

    print(password_generator(min_length,number,special_char))


if __name__=="__main__":
    main()
