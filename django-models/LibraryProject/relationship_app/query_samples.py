author_name = "Israel"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)


library_name = "Obj library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

Library.objects.get(name=library_name).books.all()
Librarian.objects.filter(library__name__iexact="obj library")