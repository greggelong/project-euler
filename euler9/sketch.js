function setup() {
  createCanvas(800, 800);
  background(0);
  brutDiophant();
 
}


function brutDiophant() {
  background(0);
  translate(width/2,height/2);
  for(let c= -500;c<500;c++){
    for(let a= -500;a<500;a++){
      for(let b= -500;b<500;b++){
        if (a**2+b**2===c**2){
          fill(255,0,0);
         
          if(a+b+c===1000){
          fill(255,255,0);
          print(a,b,c)
        }
          ellipse(a,b,5,5);
        }
   
  }
   
  }
  }
 
}