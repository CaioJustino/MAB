// Cadastro - Motorista

function ctn_cd_moto() {
  document.getElementById("part-1").style.display = 'none'
  document.getElementById("part-2").style.display = 'block'
}

function ctn_cd_moto_reverse() {
  document.getElementById("part-1").style.display = 'block'
  document.getElementById("part-2").style.display = 'none'
}

// Solicitar Viagem

// Acompanhar Viagem

function showUpdateVi() {
  document.getElementById("acompanhar-vi-cont").style.display = 'none'
  document.getElementById("update-vi").style.display = 'block'
}

function showUpdateViReverse() {
  document.getElementById("acompanhar-vi-cont").style.removeProperty('display')
  document.getElementById("update-vi").style.display = 'none'
}

function showCancelarVi() {
  document.getElementById("acompanhar-vi-cont").style.display = 'none'
  document.getElementById("cancelar-vi").style.display = 'block'
}

function showCancelarViReverse() {
  document.getElementById("acompanhar-vi-cont").style.removeProperty('display')
  document.getElementById("cancelar-vi").style.display = 'none'
}
    
// Reconhecimento de Voz - Texto em Áudio

const elementosDeTexto = document.querySelectorAll("p, h1, h2, h3, h4, h5, h6, span, a, label, button, input, th")

// On Focus

elementosDeTexto.forEach((elemento) => {
  elemento.addEventListener("focus", function lerElemento() {
    const utterance = new SpeechSynthesisUtterance()

    utterance.text = elemento.textContent

    const vozes = speechSynthesis.getVoices()
    utterance.voice = vozes[0]

    speechSynthesis.speak(utterance)
  })
})

// On Click
elementosDeTexto.forEach((elemento) => {
  elemento.style.cursor = "pointer"
  elemento.addEventListener("click", function lerElemento() {
    const utterance = new SpeechSynthesisUtterance()

    utterance.text = elemento.textContent

    const vozes = speechSynthesis.getVoices()
    utterance.voice = vozes[0]

    speechSynthesis.speak(utterance)
  })
})

// Read Placeholder

const elementosInput = document.querySelectorAll("input")

// On Focus

elementosInput.forEach((elemento) => {
  elemento.addEventListener("focus", function lerElemento() {
    const utterance = new SpeechSynthesisUtterance()
    
    if (elemento.value == "") {
      utterance.text = elemento.getAttribute("placeholder")
    }

    else {
      utterance.text = elemento.value
    }

    const vozes = speechSynthesis.getVoices()
    utterance.voice = vozes[0]

    speechSynthesis.speak(utterance)
  })
})

// Read Select Options

const elementosSelect = document.querySelectorAll("select")

// On Focus

elementosSelect.forEach((elemento) => {
  elemento.addEventListener("focus", function lerElemento() {
    const utterance = new SpeechSynthesisUtterance()

    utterance.text = elemento.options[elemento.selectedIndex].textContent

    const vozes = speechSynthesis.getVoices()
    utterance.voice = vozes[0]

    speechSynthesis.speak(utterance)
  })
})

// On Click

elementosSelect.forEach((elemento) => {
  elemento.addEventListener("click", function lerElemento() {
    const utterance = new SpeechSynthesisUtterance()
    
    utterance.text = elemento.options[elemento.selectedIndex].textContent

    const vozes = speechSynthesis.getVoices()
    utterance.voice = vozes[0]

    speechSynthesis.speak(utterance)
  })
})

// Read Image

const elementosImage = document.querySelectorAll("img")

// On Focus

elementosImage.forEach((elemento) => {
  elemento.addEventListener("focus", function lerElemento() {
    const utterance = new SpeechSynthesisUtterance()

    utterance.text = elemento.getAttribute("alt")

    const vozes = speechSynthesis.getVoices()
    utterance.voice = vozes[0]

    speechSynthesis.speak(utterance)
  })
})

// On Click

elementosImage.forEach((elemento) => {
  elemento.style.cursor = "pointer"
  elemento.addEventListener("click", function lerElemento() {
    const utterance = new SpeechSynthesisUtterance()

    utterance.text = elemento.getAttribute("alt")

    const vozes = speechSynthesis.getVoices()
    utterance.voice = vozes[0]

    speechSynthesis.speak(utterance)
  })
})

// Close CRUDs

function closeCrud(n) {
  var crud = document.querySelector(n)
  var open_form = document.querySelector("#open-form")
  var nav_painel_menu = document.querySelector("#nav-painel-menu")


  open_form.style.display = "none"
  nav_painel_menu.style.filter = "brightness(100%)"
  crud.style.display = "none"
}

// Open CRUDs

function openCrud(n) {
  var crud_open = document.querySelector(n)
  var open_form = document.querySelector("#open-form")
  var nav_painel_menu = document.querySelector("#nav-painel-menu")

  open_form.style.display = "block"
  nav_painel_menu.style.filter = "brightness(50%)"
  crud_open.style.display = "block"
  crud_open.scrollIntoView()
}

// API - MAPBOX

mapboxgl.accessToken = "pk.eyJ1IjoiY2p1c3QiLCJhIjoiY2xwNWU0bGtnMWViaTJscXZlZG5yZXpqaiJ9.ClDZFNMZlZD0tKHhAYbr-w"

// Autocomplete

const script_ac = document.getElementById('search-js');
script_ac.onload = function() {
  mapboxsearch.autofill({
    accessToken: "pk.eyJ1IjoiY2p1c3QiLCJhIjoiY2xwNWU0bGtnMWViaTJscXZlZG5yZXpqaiJ9.ClDZFNMZlZD0tKHhAYbr-w",
    options: { country: 'BR', language: 'pt', streets: 'true', house_number: 'true' }  
  })
}

// Marcador

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
  enableHighAccuracy: true
})

function successLocation(position) {
  var lng = position.coords.longitude
  var lat = position.coords.latitude


  var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [lng, lat],
    zoom: 9
  })

  const geojson = {
    type: 'FeatureCollection',
    features: [
      {
        type: 'Feature',
        geometry: {
          type: 'Point',
          coordinates: [lng, lat]
        }
      }
    ]
  }

  for (const feature of geojson.features) {
    const el = document.createElement('div')
    el.className = 'marker'

    new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates).addTo(map)
  }
}

function errorLocation() {
  console.error('Não foi possível obter a localização do usuário!')
}