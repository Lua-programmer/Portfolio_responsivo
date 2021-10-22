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

/*
Fecha o menu quando algum item é clicado
*/

const navItem = document.querySelectorAll('.nav-item');

navItem.forEach(item => {
    item.addEventListener("click", () => {
        body.classList.contains("menu=nav-active")
        ? body.classList.remove("manu-nav-active") : body.classList.replace("bi-x" , "bi-list");
        body.classList.toggle("menu-nav-active");
    });
});

/* Animação */ 

const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
  const windowTop = window.pageYOffset + window.innerHeight * 0.85 ;

  item.forEach((element) => {
    if (windowTop > element.offsetTop) {
      element.classList.add("animate");
    } else {
      element.classList.remove("animate");
    }
  });
};

animeScroll();

window.addEventListener("scroll", ()=>{
  animeScroll();
})