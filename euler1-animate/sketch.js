
let sz=10

let hw=29;

function setup() {
  createCanvas(640, 640);
  background(0)
  //showit();
  textSize(2);
  textAlign(CENTER,CENTER)
  frameRate(1)
}


function draw(){
  background(0);
  translate(100,100)
  hw ++
  if(hw>45){
    hw =30;
  }
  print(hw)
  showit();
  
  
}


function showit(){
  let count =0;
  let sum = 0;
  for (let y =0; y<hw; y++){
    
    for (let x = 0; x<hw; x++){
      count++
      stroke(0);
    // for summing
      if ( count < 1000 && (count%3 == 0 || count%5 ==0)){
        sum= sum + count
      }
      
      // for plotting
      if (count%5 == 0 && count%3 ==0 ){
        fill(255,0,255);
        //fill(105,138,143)
        
      }
      else if(count%3 == 0 ){
        fill(255,0,0);
        //fill(128,28,13);
      
      }
       else if(count%5==0){
        fill(0,0,255);
         //fill(127,146,99);
        
        
      } else{
       // fill(255,255,0)
       // fill(254,165,83)
       fill(220)
      }
      
      
        
      
      
   //  if (count == 0 ||  count == 3 || count == 5){
    //    fill(255,255,0);
  //   }
      rect(x*sz,y*sz, sz,sz)
       
    }
    
    
  }
  
  print(sum)
  print(count)
}