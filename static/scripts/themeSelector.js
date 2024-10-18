const html = document.getElementById("homeHtml");
const checkbox = document.getElementById("checkbox");

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
function checkCookie() {
    let theme = getCookie('theme')
    console.log(theme)
    if (theme === "dark") {
        html.setAttribute("data-bs-theme", "dark")
        document.getElementById('checkbox').checked = true;
    } else {
        html.setAttribute("data-bs-theme", "")
    }
}
checkbox.addEventListener("change", () => {
    if (checkbox.checked) {
        html.setAttribute("data-bs-theme", "dark");
        document.cookie = "theme=dark; path=/"
    } else {
        html.setAttribute("data-bs-theme", "");
        document.cookie = "theme=light; path=/"
    }
});

checkCookie()