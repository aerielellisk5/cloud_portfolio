// let counter = 0
// let project_one = document.querySelector('#project_one_likes')
// let project_one_like_count = 0
// project_one.addEventListener("click", increaseCount)
// let project_one_like_count_html = document.querySelector("#project_one_like_count")


// function increaseCount() {
//     project_one_like_count = project_one_like_count +1
//     project_one_like_count_html.innerHTML = project_one_like_count
//     return project_one_like_count
// }



let project_one = document.querySelector('#project_one_likes')
let project_one_like_count_html = document.querySelector("#project_one_like_count")



project_one.addEventListener("click", async function(){
    try {
        const response = await incrementCountInDatabase();
        console.log('Response from Gateway:', response);
        project_one_like_count_html.innerHTML = response



    }
    catch (error) {
        console.error('Error incrementing count:', error);
    }
})

async function incrementCountInDatabase() {
    try {

        let count = project_one_like_count_html.innerHTML
        const response = await fetch('https://4s03q312d3.execute-api.us-east-1.amazonaws.com/increase_likes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: '{}',
            // body: '{pageid:5}, can interpret that as the actual id to send to the database
            // mode: 'no-cors',
            // credentials: 'include',
        })
        // const value = await response.json()
        console.log(response.status)
        return await response.text()

    }

    catch (error) {
        throw new Error(`Failed to increment count: ${error.message}`);
    }
}


async function getCount() {
    try {
        const response = await fetch('https://4s03q312d3.execute-api.us-east-1.amazonaws.com/projects');
        console.log('was able to connect to the api layer')
        console.log('attempting to get some json back')
        const data = await response.json();
        // project_count = str(data[0])

        project_one_like_count_html.innerHTML = data
    }

    catch (error) {
        console.error('Error fetching data:', error)
    }

    
}

window.onload = getCount();