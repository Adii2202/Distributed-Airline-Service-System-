const indianCities = ["Mumbai(CSMT)", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Surat", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara","Nashik","Azamgarh","Varansi","Gorakhpur","Kushinagar","Delhi","Amritsar","London","Veitnam","Phillipins","New York","Bangkok","Rosario","Ahmedabad","Lahore"];

function populateDropdown(inputId) {
    const input = document.getElementById(inputId);
    const dropdown = document.createElement("div");
    dropdown.setAttribute("class", "dropdown-content");

    input.addEventListener("input", () => {
        const inputValue = input.value.toLowerCase();
        const filteredCities = indianCities.filter(city => city.toLowerCase().startsWith(inputValue));
        updateDropdownContent(filteredCities);
    });

    input.parentNode.insertBefore(dropdown, input.nextSibling);

    function updateDropdownContent(cities) {
        dropdown.innerHTML = '';
        cities.forEach(city => {
            const option = document.createElement("div");
            option.textContent = city;
            option.addEventListener("click", () => {
                input.value = city;
                dropdown.style.display = "none";
            });
            dropdown.appendChild(option);
        });

        if (cities.length === 0 || input.value.length === 0) {
            dropdown.style.display = "none";
        } else {
            dropdown.style.display = "block";
        }
    }
}

window.addEventListener("DOMContentLoaded", () => {
    populateDropdown("from");
    populateDropdown("to");
});
