const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item =>{
    const li = item.parentElement;
    
    item.addEventListener('click', function(){
        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
})

//TOGGLE SIDEBAR

const menuBar = document.getElementById('toggle-m');
const sideBar = document.getElementById('sidebar');

menuBar.addEventListener('click', function(){sideBar.classList.toggle('hide');})

//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