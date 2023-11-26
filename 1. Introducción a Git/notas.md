# Instalación de Git.

    sudo apt update
    sudo apt upgrade
    sudo apt install git

# Configuración de Git.

    git --version

    git config --global user.name "Gilberto-Guzman"
    git config --global user.email "josegilbertoguzmangutierrez@gmail.com"

    git config --list

# Configuración del repositorio de Git.

    mkdir Cats
    cd Cats
    git init --initial-branch=main
    git status
    ls -a

# Ayuda desde Git.

    git --help
    