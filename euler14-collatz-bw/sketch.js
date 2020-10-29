
let collatzList=[];
let collPrint;
let num =2;
function setup() {
  createCanvas(400, 800);
  background(0)
  angleMode(DEGREES);
}

function draw() {
  num=num+1;
  collatzList = []; // clear the list
  collatz(num);
  strokeWeight(3)
  // filter the canvas
  fill(0,2);
  noStroke();
  rect(0,0,width,height);
  // plot the branch
  stroke(255)
  plotit();
}

function collatz(n){   // makes list for each branch
  collatzList = [n]; // add the starting number
  // need to unshift to put them in the list backwards
  
  while (n !== 1){
    if (n%2===0){
      n=n/2;
      collatzList.unshift(n);
    }else{
      n=n*3+1
      collatzList.unshift(n);
    }
  }
 // print(collatzList)
}

function plotit(){ //plots each branch
  let len =5;
  resetMatrix();
  translate(width-width/7,height)
  for (let i of collatzList){
     if(i%2 ===0){
       rotate(-3.5)
     }else{
       rotate(6)
     }
     // set color for each branch in draw
     line(0,0,0,-len)
     translate(0,-len)    
  } 
}