Book.objects.filter(name="Mk")
library_name = "Obj library"
Library.objects.get(name=library_name).books.all()
Librarian.objects.filter(library__name__iexact="obj library")