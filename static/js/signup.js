const firstBlock = document.querySelector('.first-block')
const secondBlock = document.querySelector('.second-block')
const nextBtn = document.querySelector('#next-btn')
const backBtn = document.querySelector('#back-btn')

nextBtn.addEventListener('click', (event) => {
    firstBlock.classList.add('aside')
    secondBlock.classList.remove('aside')
})

backBtn.addEventListener('click', (event) => {
    firstBlock.classList.remove('aside')
    secondBlock.classList.add('aside')
})