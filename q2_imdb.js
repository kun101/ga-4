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
        "id": "tt6208148",
        "title": "1. Snow White",
        "year": "2025",
        "rating": "2.0"
    },
    {
        "id": "tt9104736",
        "title": "2. Housefull 5",
        "year": "2025",
        "rating": "3.7"
    },
    {
        "id": "tt10886166",
        "title": "3. 365 dni",
        "year": "2020",
        "rating": "3.3"
    },
    {
        "id": "tt34956433",
        "title": "4. Airplane 2025",
        "year": "2025",
        "rating": "2.5"
    },
    {
        "id": "tt20258920",
        "title": "5. Tin Soldier",
        "year": "2025",
        "rating": "3.4"
    },
    {
        "id": "tt31712434",
        "title": "6. Sikandar",
        "year": "2025",
        "rating": "3.8"
    },
    {
        "id": "tt34477893",
        "title": "7. Morgan: Killer Doll",
        "year": "2025",
        "rating": "3.1"
    },
    {
        "id": "tt12996154",
        "title": "8. 365 Days: This Day",
        "year": "2022",
        "rating": "2.7"
    },
    {
        "id": "tt28637027",
        "title": "9. Into the Deep",
        "year": "2025",
        "rating": "3.5"
    },
    {
        "id": "tt0128165",
        "title": "10. Blazin'",
        "year": "2001",
        "rating": "3.8"
    },
    {
        "id": "tt31723358",
        "title": "11. Pídeme lo que quieras",
        "year": "2024",
        "rating": "3.9"
    },
    {
        "id": "tt9603060",
        "title": "12. Star Trek: Section 31",
        "year": "2025",
        "rating": "3.8"
    },
    {
        "id": "tt30956852",
        "title": "13. Popeye the Slayer Man",
        "year": "2025",
        "rating": "3.5"
    },
    {
        "id": "tt6479178",
        "title": "14. Picture of Beauty",
        "year": "2017",
        "rating": "3.5"
    },
    {
        "id": "tt0118688",
        "title": "15. Batman & Robin",
        "year": "1997",
        "rating": "3.8"
    },
    {
        "id": "tt26597666",
        "title": "16. Juliet & Romeo",
        "year": "2025",
        "rating": "3.6"
    },
    {
        "id": "tt21106646",
        "title": "17. The Next 365 Days",
        "year": "2022",
        "rating": "2.9"
    },
    {
        "id": "tt29252358",
        "title": "18. Armor",
        "year": "2024",
        "rating": "3.6"
    },
    {
        "id": "tt0368226",
        "title": "19. The Room",
        "year": "2003",
        "rating": "3.6"
    },
    {
        "id": "tt33362807",
        "title": "20. Popeye's Revenge",
        "year": "2025",
        "rating": "3.5"
    },
    {
        "id": "tt24850708",
        "title": "21. Gunslingers",
        "year": "2025",
        "rating": "3.6"
    },
    {
        "id": "tt31456973",
        "title": "22. Alarum",
        "year": "2025",
        "rating": "3.3"
    },
    {
        "id": "tt34037996",
        "title": "23. Saunkan Saunkanay 2",
        "year": "2025",
        "rating": "4.0"
    },
    {
        "id": "tt7032958",
        "title": "24. Mashina lyubvi",
        "year": "2016",
        "rating": "3.7"
    },
    {
        "id": "tt2724064",
        "title": "25. Sharknado",
        "year": "2013",
        "rating": "3.3"
    }
]
*/