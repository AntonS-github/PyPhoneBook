package Les5HW_OOP.util;

import Les5HW_OOP.model.data.Contact;

import java.util.List;

public interface WriterReader {
    public List<Contact> readDB(String path);

    public void updateDB(String path, List<Contact> contacts);
}
