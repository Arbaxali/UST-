# with open(r"C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\test1.txt","w") as file:
#     # file.write("hello world")
#     data = file.read()
#     print(data)
    
# change w,r, a accordingly to add delete read file


# analogy for using slipt

with open(r"C:/Users/arbazalx/OneDrive - Intel Corporation/Desktop/javasc/flames website/test.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        word =line.split()
        print(word)

        
# Output
# PS C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website> & C:/Users/arbazalx/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/arbazalx/OneDrive - Intel Corporation/Desktop/javasc/flames website/filesnew.py"
# ['Python', 'is', 'a', 'high-level,', 'general-purpose', 'programming', 'language.', 'Its', 'design', 'philosophy', 'emphasizes', 'code', 'readability', 'with', 'the', 'use', 'of', 'significant', 'indentation.', 'Its', 'language', 'constructs', 'and', 'object-oriented', 'approach', 'aim', 'to', 'help', 'programmers', 'write', 'clear,', 'logical', 'code', 'for', 'small-', 'and', 'large-scale', 'projects.']
# []
# ['Python', 'is', 'dynamically-typed', 'and', 'garbage-collected.', 'It', 'supports', 'multiple', 'programming', 'paradigms,', 'including', 'structured', '(particularly', 'procedural),', 'object-oriented', 'and', 'functional', 'programming.', 'It', 'is', 'often', 'described', 'as', 'a', '"batteries', 'included"', 'language', 'due', 'to', 'its', 'comprehensive', 'standard', 'library.']
# []
# ['Guido', 'van', 'Rossum', 'began', 'working', 'on', 'Python', 'in', 'the', 'late', '1980s', 'as', 'a', 'successor', 'to', 'the', 'ABC', 'programming', 'language', 'and', 'first', 'released', 'it', 'in', '1991', 'as', 'Python', '0.9.0.[32]', 'Python', '2.0', 'was', 'released', 'in', '2000', 'and', 'introduced', 'new', 'features', 'such', 'as', 'list', 'comprehensions,', 'cycle-detecting', 'garbage', 'collection,', 'reference', 'counting,', 'and', 'Unicode', 'support.', 'Python', '3.0,', 'released', 'in', '2008,', 'was', 'a', 'major', 'revision', 'that', 'is', 'not', 'completely', 'backward-compatible', 'with', 'earlier', 'versions.', 'Python', '2', 'was', 'discontinued', 'with', 'version', '2.7.18', 'in', '2020.']
# ['Python', 'consistently', 'ranks', 'as', 'one', 'of', 'the', 'most', 'popular', 'programming', 'languages.']