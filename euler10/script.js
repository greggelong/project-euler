let col=0;
let row= 0;
let num =0;
let sz = 10;
let showsum;
let sum =0;


function setup(){
  createCanvas(400,400);
  background(0);
  showsum=createP("sum of primes: ", sum);
  print(num, isprime(num));
  stroke(255);
  //frameRate(20);
}

function draw(){

  if (isprime(num)){
    fill(255,0,0);
    sum = sum +num
    showsum.html(num+" "+sum);
  }else{
    fill(0,0,255);
  }
  rect(col,row,sz,sz);
  num++;
  col+=sz;
  if (col%width/sz===0){
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