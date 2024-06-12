// handle selection mechanism on the search bar
const tools = document.querySelectorAll("form.nav-search-form div")
const searchBtn = document.querySelector("form.nav-search-form button")

tools.forEach(tool => {
    tool.addEventListener('click', (event) => {
        const selection = tool.querySelector(".selection")
        if (selection.classList.contains('hidden')) {
            selection.classList.remove('hidden')
            searchBtn.classList.add('extended')
        } else {
            selection.classList.add('hidden')
            searchBtn.classList.remove('extended')
        }
    })
})

const selections = document.querySelectorAll('.selection')
selections.forEach(selection => {
    const options = selection.querySelectorAll('.option')
    options.forEach(option => {
        option.addEventListener('click', (event) => {
            let selectedOption = option.textContent
            let inputName = option.dataset.searchFor
            let input = document.querySelector(`#${inputName}`)

            input.value = selectedOption
        })
    })
})

const bars = document.querySelectorAll("div.nav-search-bar div")

bars.forEach(bar => {
    bar.addEventListener('click', (event) => {
        const header = document.querySelector('header')
        const navSearch = document.querySelector('#nav-search')
        if (header.classList.contains('header-shrink')) {
            header.classList.remove('header-shrink')
            navSearch.classList.remove('search-shrink')
        } else {
            navSearch.classList.add('search-shrink')
            header.classList.add('header-shrink')
        }
    })
})