import sys
def init_email_pers():
    if len(sys.argv) != 2:
        raise Exception("error")
    else:
        input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        data = f.readlines()
    initials_lst = []
    email_lst = []
    for email in data:
        initials_lst.append(email.split('@')[0])
        email_lst.append(email.replace('\n', ''))
    person_name_surname_lst = []
    for init in initials_lst:
        name, surname = init.split('.')
        person_name_surname_lst.append((name.capitalize(), surname.capitalize()))

    with open('employees.tsv', 'w') as f_res:
        f_res.write('name\tsurname\temail\n')
        for i, (name, surname) in enumerate(person_name_surname_lst):
            f_res.write(f"{name}\t{surname}\t{email_lst[i]}\n")

if __name__ == "__main__":
    init_email_pers()
