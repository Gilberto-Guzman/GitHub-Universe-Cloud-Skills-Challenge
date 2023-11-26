# Creación y adición (almacenamiento provisional) de un archivo.

    touch index.html
    git status

    git add .
    git status

# Realización de la primera confirmación.

    git commit index.html -m "Create an empty index.html file"
    git status
    git log

# Instalación de Vim

    sudo apt install vim

# Modifique index.html y confirme el cambio.

    vim index.html

    <h1>Our Feline Friends</h1>

    git status
    git commit -a -m "Add a heading to index.html"

# Modificación de index.html.

    vim index.html

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset='UTF-8'>
            <title>Our Feline Friends</title>
        </head>
        <body>
            <h1>Our Feline Friends</h1>
            <p>Eventually we will put cat pictures here.</p>
            <hr>
        </body>
    </html>

    git diff

    git commit -m "Add HTML boilerplate to index.html" index.html
    git diff

    vim .gitignore
    *.bak
    *~

    git add -A
    git commit -m "Make small wording change; ignore editor backups"
    git diff HEAD^

# Adición de un subdirectorio.

    mkdir CSS
    git status
    touch CSS/.git-keep
    git add CSS
    git status

# Reemplazo de un archivo.

    rm CSS/.git-keep
    cd CSS
    vim site.css

    h1, h2, h3, h4, h5, h6 { font-family: sans-serif; }
    body { font-family: serif; }

    cd ..
    vim index.html

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset='UTF-8'>
            <title>Our Feline Friends</title>
            <link rel="stylesheet" href="CSS/site.css">
        </head>
        <body>
            <h1>Our Feline Friends</h1>
            <p>Eventually we will put cat pictures here.</p>
            <hr>
        </body>
    </html>

    git status
    git add .
    git commit -m "Add a simple stylesheet"

# Enumeración de las confirmaciones.

    git log
    git log --oneline

    git log -n2

# Práctica de recuperación de un archivo eliminado.

    rm index.html
    ls
    git checkout -- index.html
    ls

# Práctica de la recuperación de un archivo eliminado: git rm

    git rm index.html
    ls
    git checkout -- index.html
    git reset HEAD index.html
    git checkout -- index.html
    ls

# Reversión de una confirmación.

    vim index.html
    
    <h1>That was a mistake!</h1>

    git commit -m "Purposely overwrite the contents of index.html" index.html
    git log -n1
    git checkout -- index.html
    vim index.html
    git revert --no-edit HEAD
    git log -n1
