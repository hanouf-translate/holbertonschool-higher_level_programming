
document.addEventListener('DOMContentLoaded', (event) => {
  const new_color = document.querySelector('header');
  new_color.addEventListener('click', function () {
    this.style.color = '#FF0000';
  });
});
