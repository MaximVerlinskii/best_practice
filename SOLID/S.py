# Single Responsibility Principle (SRP)

class Journal:
    def __init__(self) -> None:
        self.entries: list = []
        self.count: int = 0

    def add_entry(self, text: str) -> None:
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos: int) -> None:
        del self.entries[pos+1]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # def save(self, filename: str) -> None:
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename: str) -> None:
    #     pass
    #
    # def load_from_web(self, uri: str) -> None:
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal: Journal, filename: str) -> None:
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

file = r'./journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
