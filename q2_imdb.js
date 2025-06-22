// run this in a chrome dev console

const results = [];

document.querySelectorAll('li.ipc-metadata-list-summary-item').forEach((item, index) => {
    if (index >= 25) return;

    console.log(item.querySelector('.ipc-rating-star--rating'))

    // Title & IMDb ID
    const link = item.querySelector('a.ipc-title-link-wrapper');
    const href = link?.getAttribute('href') || '';
    const id = href.match(/tt\d+/)?.[0] || '';
    const title = link?.innerText.trim();

    // Year
    const yearSpan = item.querySelector('.sc-dc48a950-8');
    const year = yearSpan?.textContent.match(/\d{4}/)?.[0];

    // Rating
    const rating = item.querySelector('.ipc-rating-star--rating').innerHTML;

    if (id && title && year && rating) {
        results.push({ id, title, year, rating });
    }
});

console.log(results)
copy(results)

/*
ANSWER:
[
    {
        "id": "tt36240772",
        "title": "1. K.O.",
        "year": "2025",
        "rating": "5.8"
    },
    {
        "id": "tt35396529",
        "title": "2. Mountainhead",
        "year": "2025",
        "rating": "5.4"
    },
    {
        "id": "tt27075958",
        "title": "3. Fountain of Youth",
        "year": "2025",
        "rating": "5.7"
    },
    {
        "id": "tt27757546",
        "title": "4. Diablo",
        "year": "2025",
        "rating": "5.6"
    },
    {
        "id": "tt23060698",
        "title": "5. Clown in a Cornfield",
        "year": "2025",
        "rating": "5.7"
    },
    {
        "id": "tt27812086",
        "title": "6. Cleaner",
        "year": "2025",
        "rating": "5.1"
    },
    {
        "id": "tt21815562",
        "title": "7. The Alto Knights",
        "year": "2025",
        "rating": "5.8"
    },
    {
        "id": "tt14513804",
        "title": "8. Captain America: Brave New World",
        "year": "2025",
        "rating": "5.7"
    },
    {
        "id": "tt31176520",
        "title": "9. Eddington",
        "year": "2025",
        "rating": "5.9"
    },
    {
        "id": "tt3566834",
        "title": "10. A Minecraft Movie",
        "year": "2025",
        "rating": "5.7"
    },
    {
        "id": "tt35630700",
        "title": "11. Our Times",
        "year": "2025",
        "rating": "5.3"
    },
    {
        "id": "tt30955489",
        "title": "12. Until Dawn",
        "year": "2025",
        "rating": "5.8"
    },
    {
        "id": "tt9150192",
        "title": "13. A Working Man",
        "year": "2025",
        "rating": "5.7"
    },
    {
        "id": "tt14123284",
        "title": "14. Havoc",
        "year": "2025",
        "rating": "5.7"
    },
    {
        "id": "tt9104736",
        "title": "15. Housefull 5 A",
        "year": "2025",
        "rating": "3.7"
    },
    {
        "id": "tt32058735",
        "title": "16. Bhool Chuk Maaf",
        "year": "2025",
        "rating": "5.9"
    },
    {
        "id": "tt26342662",
        "title": "17. M3GAN 2.0",
        "year": "2025",
        "rating": "5.1"
    },
    {
        "id": "tt32194932",
        "title": "18. The Ritual",
        "year": "2025",
        "rating": "4.7"
    },
    {
        "id": "tt21317634",
        "title": "19. Bride Hard",
        "year": "2025",
        "rating": "4.5"
    },
    {
        "id": "tt27714946",
        "title": "20. The Monkey",
        "year": "2025",
        "rating": "6.0"
    },
    {
        "id": "tt30057084",
        "title": "21. Babygirl",
        "year": "2024",
        "rating": "5.8"
    },
    {
        "id": "tt16366836",
        "title": "22. Venom: The Last Dance",
        "year": "2024",
        "rating": "6.0"
    },
    {
        "id": "tt26927452",
        "title": "23. Hurry Up Tomorrow",
        "year": "2025",
        "rating": "4.7"
    },
    {
        "id": "tt28443655",
        "title": "24. Death of a Unicorn",
        "year": "2025",
        "rating": "5.9"
    },
    {
        "id": "tt31433402",
        "title": "25. Fear Street: Prom Queen",
        "year": "2025",
        "rating": "5.1"
    }
]
    */