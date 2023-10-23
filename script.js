let count = 0
let countbutton = document.querySelector('#counting')


countbutton.addEventListener("click", increaseCount);

function increaseCount() {
    count = count + 1
    console.log(count)
}



