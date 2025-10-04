document.addEventListener('DOMContentLoaded', () => {
    const tableBody = document.querySelector('#solar-system-table tbody');
    const sortSelect = document.getElementById('sort-select');
    const sortDirectionBtn = document.getElementById('sort-direction');
    let solarSystemData = [];
    let sortAscending = false;

    // Fetch and display data
    fetch('solar_system_data.json')
        .then(response => response.json())
        .then(data => {
            solarSystemData = data;
            renderTable(solarSystemData);
        });

    // Function to render the table
    function renderTable(data) {
        tableBody.innerHTML = '';
        data.forEach(object => {
            const row = `<tr>
                <td>${object.name}</td>
                <td>${object.satellites}</td>
                <td>${object.radius_km}</td>
                <td>${object.semi_major_axis_au}</td>
                <td>${object.eccentricity}</td>
                <td>${object.density_g_cm3}</td>
            </tr>`;
            tableBody.innerHTML += row;
        });
    }

    // need a function to generate the chart
    function generateChart(data) {
        const ctx = document.getElementById('solar-system-chart').getContext('2d');
        const labels = data.map(object => object.name);
        const values = data.map(object => object.radius_km);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Radius (km)',
                    data: values,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
    // Call generateChart after data is fetched and table is rendered

    // Sorting functionality
    function sortData() {
        const sortBy = sortSelect.value;
        solarSystemData.sort((a, b) => {
            if (a[sortBy] < b[sortBy]) return sortAscending ? -1 : 1;
            if (a[sortBy] > b[sortBy]) return sortAscending ? 1 : -1;
            return 0;
        });
        renderTable(solarSystemData);
    }

    sortSelect.addEventListener('change', sortData);
    sortDirectionBtn.addEventListener('click', () => {
        sortAscending = !sortAscending;
        sortDirectionBtn.textContent = sortAscending ? 'Ascending' : 'Descending';
        sortData();
    });
    
    if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js');
  });
}
    
});