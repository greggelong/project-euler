let col=0;
let row= 0;
let num =0;
let sz = 10;
let showsum;
let sum =0;
let greg;

function preload(){
  greg =loadImage("greg1.jpg");
}

function setup(){
  createCanvas(windowWidth,windowHeight-50);
  
  let sz = floor(width/100)
  greg.resize(width,height);
  greg.loadPixels();
  showsum=createP("sum of primes: ", sum);
  background(0)
  print(num, isprime(num));
  stroke(0);
  //frameRate(20);
}

function draw(){

  if (isprime(num)){
    fill(255,0,0);
    sum = sum +num
    showsum.html("prime: "+num+" sum: "+sum);
  }else{
    let colr = greg.get(col,row);
    fill(colr[0],colr[1],colr[2]);
  }
  rect(col,row,sz,sz);
  num++;
  col+=sz;
  if (col>width-sz){
   row+=sz;
   col =0;
  }
  
  if (row>height-sz){
    col =0;
    row =0
  }
  
}

function isprime(n){
  if(n === 1 || n === 0){
    return false;
  }
  else if(n === 2){
    return true;
   }else{
    for(let i = 2; i< 1+int(n**0.5); i++){
      
      if(n%i === 0){
        return false;
      }
    }
    return true;
}  
  }
