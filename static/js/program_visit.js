const mainImage = document.querySelector('.main-image-container img')

const secondaryContainers = document.querySelectorAll('.secondary-img-container')

secondaryContainers.forEach(container => {
    container.addEventListener('click', (event) => {
        const containerURL = container.querySelector('img').src
        const containerImg = container.querySelector('img')
        containerImg.src = mainImage.src
        mainImage.src = containerURL;
    })
})