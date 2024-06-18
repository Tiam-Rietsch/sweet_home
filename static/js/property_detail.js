const navSearch = document.querySelector('#nav-search')
const header = document.querySelector('header')

document.addEventListener('scroll', (event) => {
    let navSearchRect = navSearch.getBoundingClientRect()
    let listRect = propertyList.getBoundingClientRect()

    if (listRect.top < navSearchRect.top + navSearchRect.height) {
        hideSecondNavBar()
    } 
})

const main = document.querySelector('main')
main.addEventListener('click', (event) => {
    if (!navSearch.classList.contains('search-shrink')) {
        hideSecondNavBar()
    }
})

function hideSecondNavBar() {
    navSearch.classList.add('search-shrink')
    header.classList.add('header-shrink')
}