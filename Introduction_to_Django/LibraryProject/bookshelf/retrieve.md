# retrieve.md

## Django Shell Commands
```python
book = Book.objects.get(title="Mr Success")
print(f"{book.title}, {book.author}, {book.publication_year}")

Output
Mr Success, Makinde I.S, 2025