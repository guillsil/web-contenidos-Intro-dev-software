document.addEventListener('DOMContentLoaded', function() {
    const ulLists = document.querySelectorAll('.ul-article');
    const iconExpands = document.querySelectorAll('.icon-expand');
  
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
  