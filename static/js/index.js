const url_atual = window.location.pathname;

const navigation = document.querySelectorAll('#navigation > li > a');

navigation.forEach(navItem => {
    if(navItem.getAttribute('href') == url_atual) {
        navItem.classList.add('active');
    }
});
