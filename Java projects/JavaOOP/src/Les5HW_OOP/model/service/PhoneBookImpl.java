package Les5HW_OOP.model.service;
import Les4HW_OOP.view.ConsoleViewImpl;
import Les4HW_OOP.view.View;
import Les5HW_OOP.config.Config;
import Les5HW_OOP.model.data.Contact;
import Les5HW_OOP.util.WriterReader;
import Les5HW_OOP.util.WriterReaderCSVImpl;
import Les5HW_OOP.util.WriterReaderTXTImpl;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PhoneBookImpl implements PhoneBook {
    private List<Contact> contactList;
    private WriterReader wr;

    public PhoneBookImpl(WriterReader writerReader) {
        this.contactList = new ArrayList<>();
        wr = writerReader;
    }

    public PhoneBookImpl() {
    }

    @Override
    public void loadContacts(String path) {
        contactList = wr.readDB(Config.path);
    }

    @Override
    public String printAllContacts() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n");
        int i = 0;
        for (Contact contact :
                contactList) {
            sb.append(i++).append("-\t").append(contact).append("\n");
        }
        return sb.toString();
    }

    @Override
    public List<Contact> searchContact(String string) {
        List<Contact> result = new ArrayList<>();
        for (Contact contact :
                contactList) {
            if (contact.getUser().getFirstName().equals(string) || contact.getUser().getLastName().equals(string)) {
                result.add(contact);
            }
        }
        return result;
    }

    @Override
    public void addContact(Contact contact) {
        contactList.add(contact);
        wr.updateDB(Config.path, contactList);
    }

    @Override
    public void removeContact(int index) {
        contactList.remove(contactList.get(index));
        wr.updateDB(Config.path, contactList);
    }

    @Override
    public boolean isExist(Contact contact) {
        return contactList.contains(contact);
    }

    public List<Contact> getContactList() {
        return contactList;
    }

    @Override
    public void export(String path) {
        try {
            View tempView = new ConsoleViewImpl ();
            File file = new File(path);
            if (file.createNewFile()) {
                if (path.endsWith(".csv")) {
                    WriterReader tempWR = new WriterReaderCSVImpl ();
                    tempWR.updateDB(path, contactList);
                } else if (path.endsWith(".txt")) {
                    WriterReader tempWR = new WriterReaderTXTImpl ();
                    tempWR.updateDB(path, contactList);
                } else {
                    tempView.set("?????????????? ???????????????????????? ????????????.");
                }
            } else {
                tempView.set("???????? ?? ?????????? ?????????????????? ?????? ????????????????????.");
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
