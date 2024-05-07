document.addEventListener('DOMContentLoaded', function() {
    const iconExpands = document.querySelectorAll('.icon-expand');
    const nav = document.querySelector('#nav');
    const abrirMenu = document.querySelector('#abrir-menu');
    const cerrarMenu = document.querySelector('#cerrar-menu');

    abrirMenu.addEventListener('click', function() {
      nav.classList.add('visible');
      abrirMenu.style.display = 'none';
    });


    cerrarMenu.addEventListener('click', function() {
      nav.classList.remove('visible');
      abrirMenu.style.display = 'block';
    });

    function toggleElement() {
      const ulList = this.parentNode.nextElementSibling;
      if (ulList.style.display === 'none' || ulList.style.display === '') {
        ulList.style.display = 'block';
      } else {
        ulList.style.display = 'none';
      }
    }
  
    iconExpands.forEach(function(iconExpand) {
      iconExpand.addEventListener('click', toggleElement);
    });
  });
  