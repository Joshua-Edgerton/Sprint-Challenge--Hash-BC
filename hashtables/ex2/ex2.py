#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # For each element in length
    # "i" will be used to iterate through elements
    for i in range(length):
        # Insert the ticket source and destination into the table
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # For each element in length
    # "i" will be used to iterate through elements
    for i in range(length):
        print("Step 1 - Length of route array ->", len(set(route)))
        # If the length equals 1
        if len(set(route)) == 1:
            # That index in route equals the hashtable with a key of none
            route[i] = hash_table_retrieve(hashtable, "NONE")
            print("Step 2 - Route which has 'None' as key ->", route[i])
        # Otherwise
        else:
            # That index in route equals the retrieved hashtable
            # which has a key of the indexed route - 1
            print("Step 3 - Routes previous destination ->", route[i - 1])
            # Set this index route to equal the hashtabled route 
            # Which key matches the previous routes destination
            route[i] = hash_table_retrieve(hashtable, route[i - 1])
   
    print(route[0:])
    # Return routes minus the last empty destination
    return route[:-1]

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(reconstruct_trip(tickets, 10))