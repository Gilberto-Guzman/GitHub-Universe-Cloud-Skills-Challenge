# Clonación de un repositorio.

    cd ..
    mkdir Alice
    cd Alice
    git clone ../Cats .

# Corroboración del estado de los datos.

    pwd
    git pull

# Realización de un cambio y envío de una solicitud de incorporación de cambios.

    git config user.name "Alice"
    git config user.email "alice@contoso.com"

    vim CSS/site.css

    body { font-family: serif; background-color: #F0FFF8; }

    git commit -a -m "Change background color to light blue"

# Creación de un remoto y finalización de la solicitud de incorporación de cambios.

    cd ../Cats
    git remote add remote-alice ../Alice/Cats
    git pull remote-alice main

# Creación de un repositorio vacío.

    cd ..
    mkdir Shared.git
    cd Shared.git
    git init --bare

    cd ../Cats
    git remote add origin ../Shared.git
    git push origin main
    git branch --set-upstream-to origin/main

# Configuración para colaboradores.

    cd ..
    mkdir Bob
    cd Bob
    git clone ../Shared.git .

    cd ../Alice
    git remote set-url origin ../Shared.git

# Inicio de la colaboración.

    cd ../Bob
    git config user.name Bob
    git config user.email bob@contoso.com

    vim index.html

    <footer><hr>Copyright (c) 2021 Contoso Cats</footer>

    git commit -a -m "Put a footer at the bottom of the page"
    git push

    cd ../Alice
    vim index.html

    <nav><a href="./index.html">home</a></nav>

    vim CSS/site.css

    nav { background-color: #C0D8DF; }

    git pull
    git diff origin -- index.html
    git stash

    vim CSS/site.css
    nav, footer { background-color: #C0D8DF; }

    git commit -a -m "Stylize the nav bar"
    git push

    cd ../Cats
    git pull

    cd ../Bob
    git pull

    sudo apt update
    sudo apt install zip

    git pull ../Bob
    git pull ../Alice

    cd ..
    zip -r Cats.zip Cats