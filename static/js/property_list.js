const propertyList = document.querySelector('.property-list-container')
const propertyListYPos = propertyList.getBoundingClientRect().top
document.addEventListener('scroll', (event) => {
    const navSearch = document.querySelector('#nav-search')
    const header = document.querySelector('header')
    
    let navSearchRect = navSearch.getBoundingClientRect()
    let listRect = propertyList.getBoundingClientRect()

    if (listRect.top < navSearchRect.top + navSearchRect.height) {
        navSearch.classList.add('search-shrink')
        header.classList.add('header-shrink')
    } 

    if (propertyListYPos == listRect.top) {
        navSearch.classList.remove('search-shrink')
        header.classList.remove('header-shrink')
    }
})