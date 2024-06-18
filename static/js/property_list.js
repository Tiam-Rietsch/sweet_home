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

const cards = document.querySelectorAll('.property-card')
cards.forEach(card => {
    card.addEventListener('click', (event) => {

        changeLocation(event, card.dataset.propertyUrl)
    }) 
})

const cardLinks = document.querySelectorAll('.card-link')
cardLinks.forEach(link => {

    link.addEventListener('click', (event) => {
        event.preventDefault()

        cardLinks.forEach(link => link.classList.remove('selected'))
        link.classList.add('selected')
        const imgIndex = link.dataset.imgIndex;
        const img = link.parentElement.parentElement.querySelector(`.card-img img:nth-child(${imgIndex})`)

        img.scrollIntoView({
            'behavior': "smooth",
            'block': 'nearest'
        })

        return false
    })
})

function changeLocation(event, url) {
    if (!event.target.classList.contains('card-link')) {
        window.location.href = url
    }
}