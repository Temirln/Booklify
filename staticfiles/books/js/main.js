let closeBtn = document.getElementById('close');
let nav = document.getElementById('nav');
let openBtn = document.getElementById('open');

closeBtn.onclick = function(){
    nav.style.display = 'none';
}

openBtn.onclick = function(){
    nav.style.display = 'flex';
}
let searchicon = document.querySelector(".search-container");
let searchbox = document.querySelector(".search-box");

searchicon.onclick = function(){
	searchbox.classList.toggle('activesearch');
}
for (let i = 0;i <more.length; i++) {
	more[i].addEventListener('click',function(){
		more[i].previousElementSibling.classList.toggle('activep');
		more[i].classList.toggle('activemore');
	})
}

window.addEventListener("scroll", function(){
	var stickymenu = document.querySelector(".menu-head");
	stickymenu.classList.toggle("active-menu", window.scrollY > 200);
})
