let counter = 0
let project_one = document.querySelector('#project_one_likes')
let project_one_like_count = 0
project_one.addEventListener("click", increaseCount)
let project_one_like_count_html = document.querySelector("#project_one_like_count")


function increaseCount() {
    project_one_like_count = project_one_like_count +1
    project_one_like_count_html.innerHTML = project_one_like_count
    return project_one_like_count
}

// checkout the onload for the document


function onloadcounter () {
    counter = counter + 1
    console.log(counter)
    return counter
}

