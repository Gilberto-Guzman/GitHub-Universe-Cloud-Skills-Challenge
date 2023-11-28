# Creación de un repositorio vacío compartido.

    mkdir Shared.git
    cd Shared.git

    sudo apt update
    sudo apt upgrade
    sudo apt install git

    git init --bare
    git symbolic-ref HEAD refs/heads/main

# Clonación del repositorio compartido para Bob.

    cd ..
    mkdir Bob

    cd Bob
    git clone ../Shared.git .
    git config user.name Bob
    git config user.email bob@contoso.com
    git symbolic-ref HEAD refs/heads/main

# Incorporación de archivos base.

    touch index.html
    mkdir Assets
    touch Assets/site.css
    git add .
    git commit -m "Create empty index.html and site.css files"

    sudo apt install vim

    vim index.html

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset='UTF-8'>
            <title>Our Feline Friends</title>
            <link rel="stylesheet" href="CSS/site.css">
        </head>
        <body>
            <nav><a href="./index.html">home</a></nav>
            <h1>Our Feline Friends</h1>
            <p>Eventually we will put cat pictures here.</p>
            <footer><hr>Copyright (c) 2021 Contoso Cats</footer>
        </body>
    </html>

    cd Assets
    vim site.css

    cd ..
    git add .
    git commit -m "Add simple HTML and stylesheet"
    git push --set-upstream origin main

    git config --global push.default simple

# Creación de una rama para Alice.

    cd ..
    mkdir Alice

    cd Alice
    git clone ../Shared.git .
    git config user.name Alice
    git config user.email alice@contoso.com

    ls
    git status

    git branch add-style
    git checkout add-style

    vim Assets/site.css

    .cat { max-width: 40%; padding: 5 }

    git commit -a -m "Add style for cat pictures"

    git merge --ff-only add-style
    git push

# Combinación de la rama de Bob.

    cd ../Bob
    git checkout -b add-cat

    wget https://github.com/MicrosoftDocs/mslearn-branch-merge-git/raw/main/git-resources.zip
    sudo apt-get install unzip
    unzip git-resources.zip

    mv bobcat2-317x240.jpg Assets/bobcat2-317x240.jpg
    rm git-resources.zip
    rm bombay-cat-180x240.jpg

    vim index.html

    <img src="Assets/bobcat2-317x240.jpg" />

    git status

    git add .
    git commit -a -m "Add picture of Bob's cat"

    git checkout main
    git pull

    git merge add-cat --no-edit
    git push

    cd ../Alice
    git pull

# Creación de ramas para Alice y Bob.

    cd Alice
    git checkout -b add-cat
    cd ../Bob
    git checkout -b style-cat

# Realización de un cambio como Alice.

    cd ../Alice
    wget https://github.com/MicrosoftDocs/mslearn-branch-merge-git/raw/main/git-resources.zip
    unzip git-resources.zip

    mv bombay-cat-180x240.jpg Assets/bombay-cat-180x240.jpg
    rm git-resources.zip
    rm bobcat2-317x240.jpg

    vim index.html

    <img class="cat" src="Assets/bombay-cat-180x240.jpg" />

    git add Assets
    git commit -a -m "Add picture of Alice's cat"
    git checkout main
    git pull
    git merge --ff-only add-cat
    git push

# Realización de un cambio como Bob.

    cd ../Bob

    vim index.html

    <img class="cat" src="Assets/bobcat2-317x240.jpg" />

    git commit -a -m "Style Bob's cat"
    git checkout main
    git pull
    git merge style-cat

# Resolución del conflicto de combinación.

    vim index.html

    quita esto:
    <<<<<<< HEAD
    =======
    >>>>>>> style-cat

    git add index.html
    git commit -a -m "Style Bob's cat"
    git push

    cd ../Alice
    git pull