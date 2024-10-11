const html = document.getElementById("homeHtml");
const checkbox = document.getElementById("checkbox");
checkbox.addEventListener("change", () => {
    if (checkbox.checked) {
        html.setAttribute("data-bs-theme", "dark");
    } else {
        html.setAttribute("data-bs-theme", "");
    }
});
