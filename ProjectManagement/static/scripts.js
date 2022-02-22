function disasterfilter(){
    document.getElementById('_id_state').reset();
    document.getElementById('_id_disaster_number').reset();
    document.getElementById('_id_declaration_date').reset();
    document.getElementById('id_disaster_closeout_status').reset();
    document.getElementById("id_hmgp_closeout_status").reset();
    document.getElementById('filterbtn1').click();
    };

function projectfilter(){
    document.getElementById('id_state').reset();
    document.getElementById('id_disaster_number').reset();
    document.getElementById('id_project_identifier').reset();
    document.getElementById('id_project_title').reset();
    document.getElementById('id_type').reset();
    document.getElementById('id_county').reset();
    document.getElementById('id_subgrantee').reset();
    document.getElementById('filterbtn2').click();
    }

function hideshow(){
    var x = document.getElementById("btn1");
    x.style.display ="none"
    var y = document.getElementById("btn2");
    y.style.display="visible"
}
 

   