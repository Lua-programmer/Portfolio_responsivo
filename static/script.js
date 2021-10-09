/*Abre e fecha menu lateral em modo mobile*/

/*
Criando constantes que irão pegar elementos do HTML
*/
const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector("body");

/* Nesse elemento vamos adicionar um evento de clique */
menuMobile.addEventListener("click", () => {
    // Olhar na classList se contem bi-list
    menuMobile.classList.contains("bi-list")
    // Se tiver, vamos trocar a bi-list por bi-x
    ? menuMobile.classList.replace("bi-list", "bi-x") : menuMobile.classList.replace("bi-x", "bi-list");
    body.classList.toggle("menu-nav-active");
});