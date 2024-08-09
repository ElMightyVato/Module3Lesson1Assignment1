# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

# This is my sample to use for my program
tickets = {}

def open_ticket(tickets, customer_name, issue_description):
    new_id = max(tickets.keys()) + 1 if tickets else 1 # This is helping me create ticket ID numbers
    tickets[new_id] = {"customer_name": customer_name, "issue_description": issue_description, "status": "open"}
    print(f"Ticket {new_id} opened for {customer_name}")

def update_status(tickets, ticket_id, new_status):
    if ticket_id in tickets: # This will go through my dictionary and number each row 
        tickets[ticket_id]["status"] = new_status # This will update status to new status 
        print(f"Ticket {ticket_id} status updated to {new_status}")
    else:
        print(f"Ticket {ticket_id} not in system.")

def display_tickets(tickets, status_filter=None):
    for ticket_id, ticket_info in tickets.items(): #This will start a loop for me to go through every ticket in the dictionary
        if status_filter is None or ticket_info["status"] == status_filter: #This will assit in filtering the status
            print(f"ID: {ticket_id}, Customer: {ticket_info['customer_name']}, Issue: {ticket_info['issue_description']}, Status: {ticket_info['status']}")

def main():
    while True:
        print("Customer Service Ticket System")
        print("1. Display all tickets")
        print("2. Display tickets by status")
        print("3. Open a new ticket")
        print("4. Update ticket status")
        print("5. Exit")

        choice = input("Choose an option from the choices displayed: ")
        
        if choice == "1":
            display_tickets(tickets)  # this will be to display all tickets that's why I only target tickets when I apply the function

        elif choice == "2":
            status_filter = input("How would you like to filter the tickets? (open/closed) ").strip().lower()
            if status_filter in ["open", "closed"]:
                display_tickets(tickets, status_filter)
            else: 
                print("invalid statusl. Please enter 'open' or 'closed'")

        elif choice == "3":
            customer_name = input("Enter customer name: ").strip()
            issue_description = input("Enter issue description: ").strip()
            open_ticket(tickets, customer_name, issue_description)
        
        elif choice == "4":
            try: 
                ticket_id = int(input("Enter ticket ID to update: ").strip())
                new_status = input("Enter new status (open/closed): ").strip().lower()
                if new_status in ["open", "closed"]:
                    update_status(tickets, ticket_id, new_status)
                else:
                    print("Invalid status. Please enter 'open' or 'closed'.")
            except ValueError:
                print("Invalid ticket ID. Please enter a number.")

        elif choice == "5":
            print("Thanks for using my program.....GOOD BYE!")
            break

main()