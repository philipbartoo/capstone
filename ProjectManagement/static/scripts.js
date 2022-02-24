


document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
    const dropZoneElement = inputElement.closest(".drop-zone");
  dropZoneElement.addEventListener("click", (e) => {
      inputElement.click();
    });
  inputElement.addEventListener("change", (e) => {
      if (inputElement.files.length) {
        updateThumbnail(dropZoneElement, inputElement.files[0]);
      }
    });
  dropZoneElement.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropZoneElement.classList.add("drop-zone--over");
    });
  ["dragleave", "dragend"].forEach((type) => {
      dropZoneElement.addEventListener(type, (e) => {
        dropZoneElement.classList.remove("drop-zone--over");
      });
    });
  dropZoneElement.addEventListener("drop", (e) => {
      e.preventDefault();
  if (e.dataTransfer.files.length) {
        inputElement.files = e.dataTransfer.files;
        updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
      }
  dropZoneElement.classList.remove("drop-zone--over");
    });
  });
  function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");
  // First time - remove the prompt
    if (dropZoneElement.querySelector(".drop-zone__prompt")) {
      dropZoneElement.querySelector(".drop-zone__prompt").remove();
    }
  // First time - there is no thumbnail element, so lets create it
    if (!thumbnailElement) {
      thumbnailElement = document.createElement("div");
      thumbnailElement.classList.add("drop-zone__thumb");
      dropZoneElement.appendChild(thumbnailElement);
    }
  thumbnailElement.dataset.label = file.name;
  // Show thumbnail for image files
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
  reader.readAsDataURL(file);
      reader.onload = () => {
        thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
      };
    } else {
      thumbnailElement.style.backgroundImage = null;
    }
  }; 

  





function disasterfilter() {
   
    document.getElementById('div_id_state').value="";
    document.getElementById('div_id_disaster_number').value="";
    document.getElementById('div_id_declaration_date').value="";
    document.getElementById('div_id_disaster_closeout_status').value="";
    document.getElementById("div_id_hmgp_closeout_status").value="";
    
    var pagebutton=document.getElementById("filterbtn1");
    pagebutton.click();
    };

function projectfilter(){
    document.getElementById('id_state').value("");
    document.getElementById('id_disaster_number').value("");
    document.getElementById('id_project_identifier').value("");
    document.getElementById('id_project_title').value("");
    document.getElementById('id_type').value("");
    document.getElementById('id_county').value("");
    document.getElementById('id_subgrantee').value("");
    document.getElementById('filterbtn2').click();
    };

function hideshow(){
    var x = document.getElementById("btn1");
    x.style.display ="none"
    var y = document.getElementById("btn2");
    y.style.display="visible"
};