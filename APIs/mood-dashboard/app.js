const cache={};
let loading=false;
let currentCity=null;

const moods={
 feliz:{bg:"linear-gradient(135deg,#FFD93D,#FF9A3D)",movie:"comedy",music:"pop",book:"happiness"},
 triste:{bg:"linear-gradient(135deg,#6C5B7B,#355C7D)",movie:"drama",music:"blues",book:"sadness"},
 energetico:{bg:"linear-gradient(135deg,#F08A5D,#B83B5E)",movie:"action",music:"rock",book:"motivation"},
 nostalgico:{bg:"linear-gradient(135deg,#B83B5E,#6C5B7B)",movie:"romance",music:"classical",book:"memory"},
 relajado:{bg:"linear-gradient(135deg,#6A8D73,#A8D5BA)",movie:"family",music:"ambient",book:"meditation"}
};

const cities=[
 {name:"Tokyo",lat:35,lon:139,country:"Japón"},
 {name:"Paris",lat:48.8,lon:2.3,country:"Francia"},
 {name:"Lima",lat:-12,lon:-77,country:"Perú"},
 {name:"New York",lat:40,lon:-74,country:"EE.UU."}
];

document.querySelectorAll(".mood-btn")
.forEach(b=>b.addEventListener("click",handleMood));

async function handleMood(e){
 if(loading)return;
 loading=true;

 const key=e.currentTarget.dataset.mood;
 const mood=moods[key];

 document.querySelectorAll(".mood-btn")
 .forEach(b=>b.classList.remove("active"));
 e.currentTarget.classList.add("active");

 document.body.style.background=mood.bg;

 if(cache[key]){
  render(cache[key]);
  loading=false;
  return;
 }

 currentCity=cities[Math.floor(Math.random()*cities.length)];
 showLoader(true);

 try{
  const [weather,movie,music,book]=await Promise.all([
   fetchWeather(),
   fetchMovie(mood.movie),
   fetchMusic(mood.music),
   fetchBook(mood.book)
  ]);

  const data={weather,movie,music,book};
  cache[key]=data;
  render(data);

 }catch{
  showError("Error cargando datos");
 }

 showLoader(false);
 loading=false;
}

// clima
async function fetchWeather(){
 try{
  const {lat,lon}=currentCity;
  const r=await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`);
  const d=await r.json();
  return `${d.current_weather.temperature}°C · viento ${d.current_weather.windspeed} km/h`;
 }catch{
  return "Clima no disponible";
 }
}

// pelicula
async function fetchMovie(g){
 const valid=["action","animation","comedy","drama","family","horror","mystery","romance","scifi","western"];
 if(!valid.includes(g))g="drama";

 try{
  const r=await fetch(`https://api.sampleapis.com/movies/${g}`);
  const arr=await r.json();
  if(!arr.length)throw 0;
  return arr[Math.floor(Math.random()*arr.length)];
 }catch{
  return{
   title:"Película recomendada",
   year:"2024",
   posterURL:"https://picsum.photos/id/237/300/450"
  };
 }
}

// musica local
async function fetchMusic(g){
 const lib={
  pop:[{title:"Blinding Lights",artist:"The Weeknd",albumCover:"https://picsum.photos/id/1003/300/300"}],
  blues:[{title:"The Thrill is Gone",artist:"B.B. King",albumCover:"https://picsum.photos/id/1025/300/300"}],
  rock:[{title:"Bohemian Rhapsody",artist:"Queen",albumCover:"https://picsum.photos/id/1062/300/300"}],
  classical:[{title:"Moonlight Sonata",artist:"Beethoven",albumCover:"https://picsum.photos/id/1043/300/300"}],
  ambient:[{title:"Weightless",artist:"Marconi Union",albumCover:"https://picsum.photos/id/1056/300/300"}]
 };
 const arr=lib[g]||lib.pop;
 return arr[Math.floor(Math.random()*arr.length)];
}

// libro
async function fetchBook(q){
 try{
  const r=await fetch(`https://openlibrary.org/search.json?q=${q}&limit=1`);
  const d=await r.json();
  const b=d.docs?.[0];
  if(!b)throw 0;

  return{
   title:b.title,
   author:b.author_name?.[0]||"Autor desconocido",
   cover:b.cover_i
    ?`https://covers.openlibrary.org/b/id/${b.cover_i}-L.jpg?default=false`
    :"https://picsum.photos/id/1003/300/450"
  };
 }catch{
  return{
   title:"Libro recomendado",
   author:"Autor",
   cover:"https://picsum.photos/id/1003/300/450"
  };
 }
}

// render
function render(data){
 const dash=document.getElementById("dashboard");
 dash.innerHTML=`
  ${card("🎬 Película",data.movie.title,data.movie.posterURL,data.movie.year)}
  ${card("🎵 Música",data.music.title,data.music.albumCover,data.music.artist)}
  ${card("📚 Libro",data.book.title,data.book.cover,data.book.author)}
 `;

 document.getElementById("location-info").innerHTML=
 `<h2>${currentCity.name}, ${currentCity.country}</h2><p>${data.weather}</p>`;
 document.getElementById("location-info").classList.remove("hidden");
}

function card(t,txt,img,sub=""){
 return`
 <div class="card">
  <h3>${t}</h3>
  <img src="${img}">
  <b>${txt}</b>
  <div>${sub||""}</div>
 </div>`;
}

function showLoader(v){
 document.getElementById("loader").classList.toggle("hidden",!v);
}

function showError(m){
 const el=document.getElementById("error-message");
 el.textContent=m;
 el.classList.remove("hidden");
}