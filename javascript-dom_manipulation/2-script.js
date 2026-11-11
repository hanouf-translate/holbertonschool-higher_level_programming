document.addEventListener('DOMContentLoaded', (event) => {
  const element = document.querySelector('#red_header');

  element.addEventListener('click', function () {
    element.classList.add('red');
  });
});
