function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function editLevel() {

    s_level = document.getElementById("edit-level");
    e_level_name = document.getElementById("edit_level_name");
    e_level_id = document.getElementById("edit_level_id");
    e_level_delete = document.getElementById("edit_level_delete");
    e_level_country = document.getElementById("edit_level_country");
    e_level_isSenior = document.getElementById("edit_level_isSenior");
    e_level_isMale = document.getElementById("edit_level_isMale");
    e_level_isNational = document.getElementById("edit_level_isNational");

    // If user wants to create a new level

    if (s_level.options[s_level.selectedIndex].value == "new_level") {

            e_level_name.disabled = false;
            e_level_country.disabled = false;
            e_level_isSenior.disabled = false;
            e_level_isMale.disabled = false;
            e_level_isNational.disabled = false;
            e_level_delete.disabled = true;
    }

    // If selected value exists, fetch data for editing

    else {

       fetch("https://fbscanner.io/apis/levels/" + s_level.options[s_level.selectedIndex].value + "/")
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                e_level_name.value = data.name;
                e_level_id.value = data.id;
                e_level_country.value = data.country;
                e_level_isSenior = data.isSenior;
                e_level_isMale = data.isMale;
                e_level_isNational = data.isNational;
                e_level_name.disabled = false;
                e_level_country.disabled = false;
                e_level_isSenior.disabled = false;
                e_level_isMale.disabled = false;
                e_level_isNational.disabled = false;
                e_level_delete.disabled = false;

        })
            .catch((error) => {
                console.error('Error:', error);
        });

    }
}

function editLevelButton() {

    var r = confirm("Do you want to save data?");
    if (r == true) {
        data = {
            "name": e_level_name.value,
            "country": e_level_country.value,
            "isSenior": e_level_isSenior,
            "isMale": e_level_isMale,
            "isNational": e_level_isNational,
        }

        fetch("https://fbscanner.io/apis/levels/" + e_level_id + "/", {

          method: 'PATCH', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body: JSON.stringify(data),
        })

        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            window.alert("Data saved!");
            e_level_name.value = "";
            e_level_id.value = "";
            for (let i=e_level_country.length -1; i>0; i--) {
                    e_level_country.remove(i);
                }
            e_level_country.selectedIndex = "0";
            e_level_isSenior = false;
            e_level_isMale = false;
            e_level_isNational = false;
            e_level_name.disabled = true;
            e_level_country.disabled = true;
            e_level_isSenior.disabled = true;
            e_level_isMale.disabled = true;
            e_level_isNational.disabled = true;
            e_level_delete.disabled = true;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }

}

function deleteLevelButton() {

}