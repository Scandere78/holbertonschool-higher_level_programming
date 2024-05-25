#!/usr/bin/python3

class VerbodeList(list):

    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")
            super().remove(item)
        else:
            print(f"Item {item} not found in the list.")

    def pop(self, index=-1):
        if index < len(self):
            item = self[index]
            super().pop(index)
            print(f"Popped {item} from the list.")
        else:
            print(f"Index {index} out of range. Cannot pop from the list.")
