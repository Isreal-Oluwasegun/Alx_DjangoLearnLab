Book.objects.filter(name="Mk")
Library.objects.get(name="Obj library").books.all()
Librarian.objects.filter(library__name__iexact="obj library")