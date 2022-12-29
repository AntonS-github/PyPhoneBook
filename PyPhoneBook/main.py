from models.data import ContactsRepo
from models.service import PhoneBookService
from views.view import ConsoleView



def main():
    repository = ContactsRepo()
    service = PhoneBookService(repository)
    console = ConsoleView(service)
    console.run()


if __name__ == "__main__":
    main()
