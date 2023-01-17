function removeElementsByClass(className){
   const elements = document.getElementsByClassName(className);
   while(elements.length > 0){
       elements[0].parentNode.removeChild(elements[0]);
   }
}

removeElementsByClass('ranks');
removeElementsByClass('files');

var firstCell = document.getElementsByTagName('cg-resize')[0];
firstCell.remove();

const interval = setInterval(function() {
   collection = document.getElementsByClassName("last-move"); 
   collection[0].className = "a"; 
   collection[1].className = "a";  
 }, 50); 

const interval2 = setInterval(function() {
   collection2 = document.getElementsByClassName("check");
   collection2[0].className = "a";
}, 50); 