const form = document.getElementById('form');

function retrieveFormValue(event) {
event.preventDefault();

const vid = form.querySelector('[name="vid"]');
const rost = form.querySelector('[name="rost"]');

if (vid.value == 'Слалом'){
if (Number(rost.value)<=165){outed.innerHTML=155;}
if (Number(rost.value)<175 && Number(rost.value)>165){outed.innerHTML=160;}
if (Number(rost.value)<180 && Number(rost.value)>=175){outed.innerHTML=167;}
if (Number(rost.value)>180){outed.innerHTML=170;}
}
if(vid.value == 'Универсал'){outed.innerHTML= Number(rost.value)-6;}
if(vid.value == 'Фрирайд'){
outed.innerHTML= Number(rost.value)+7;}
}

form.addEventListener('submit', retrieveFormValue)