import sys

def message_to():
    if len(sys.argv) != 2:
        raise Exception("error")

    email_input = sys.argv[1]
    with open('employees.tsv', 'r') as f:
            lines = f.readlines()
    for line in lines[1:]:
        name, surname, email = line.strip().split('\t')
        if email == email_input:
            letter = f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires."
            print(letter)
            break
    else:
        print("email doesn`t exist")
        

if __name__ == "__main__":
    message_to()



