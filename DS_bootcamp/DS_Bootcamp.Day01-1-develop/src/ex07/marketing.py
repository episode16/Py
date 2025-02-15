import sys
def call_center(clients, recipients):
    clients = set(clients)
    recipients = set(recipients)
    return list(clients - recipients)

def potential_clients(clients, participants):
    clients = set(clients)
    participants = set(participants)
    return list(participants - clients)

def loyalty_program(clients, participants):
    clients = set(clients)
    participants = set(participants)
    return list(clients - participants)

def main():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill\_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if len(sys.argv) != 2:
        raise Exception("error")
    var = sys.argv[1]
    var = var.replace(' ', '')
    words = [word.strip() for word in var.split(',')]
    call_center_lst = list()
    potential_clients_lst = list()
    loyalty_program_lst = list()
    for word in words:
        if word == 'call_center':
            call_center_lst += call_center(clients, recipients)
        elif word == 'potential_clients':
            potential_clients_lst += potential_clients(clients, participants)
        elif word == 'loyalty_program':
            loyalty_program_lst += loyalty_program(clients, participants)
        else:
            raise Exception("error")
    if len(call_center_lst) != 0:
        print('LIST OF CALL CENTER:')
        print("\n".join(call_center_lst))
    if len(potential_clients_lst) != 0:
        print('LIST OF POTENTIAL CLIENTS:')
        print("\n".join(potential_clients_lst))
    if len(loyalty_program_lst):
        print('LIST OF LOYALTY PROGRAM:')
        print("\n".join(loyalty_program_lst))

if __name__ == "__main__":
    main()