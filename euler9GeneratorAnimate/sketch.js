let dio;

function setup() {
  createCanvas(800, 800);
  background(0);
  rectMode(CENTER);
  angleMode(DEGREES);
  colorMode(HSB,300);
  ;

  dio = brutDiophant();

 
}


function draw(){
  
  translate(width/2,height/2);
  
  //rotate(frameCount%360);  // rotate here
  dio.next();
  
  if (dio.next().done){
    background(0);
    dio = brutDiophant();
  }
}

// generator function allows you to animate
// values created inside of for loops
// it yields values to the draw loop and the draw loop
// asks for next values
// if the same thing was done in a normal function
// each frame would print the complete picture
// this is good to animate algorithms or for displaying 
// things that are computationally slow.  like this.
// I should revisit the Mandelbrot set and use a generator function


function* brutDiophant() {
  
  for(let c= 0;c<360;c++){   // if c starts at 0 it moves from the center out
    for(let a= -360;a<+360;a++){     // the a and b are plotted as x and y
      for(let b= -360;b<360;b++){
        if (a**2+b**2===c**2){
          fill(c,300,300);
          //stroke(300-c,300,300);
          stroke(0);
         
          if(a+b+c===1000){
          fill(255);
          print(a,b,c)
        }
          push();
          translate(a,b);
          rotate(frameCount%360); 
          rect(0,0,10,10);
          pop();
          //ellipse(a,b,10,10);
           
          yield;
        }
   
  }
   
  }
  }
 
}