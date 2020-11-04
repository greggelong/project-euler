let sz =20;
let rowcol =10;

let ball;

let instr = [];
let nextinst =0;

let myturtle;


function setup() {
  createCanvas(400, 400);
  background(0);
  rectMode(CENTER);
  textSize(16)
  frameRate(10);
  myturtle = turtle();
  instr = findPermutations('RRRRRRRRRDDDDDDDDD');
  //console.log(instr)
  stroke(0,255,0);
  translate(50,50);
  showlatt();
  ball = createVector(0,0) 
  rect(ball.x,ball.y, sz,sz)
  nextinst = floor(random(instr.length))
  fill(0,255,0)
  text("path: "+nextinst+" "+instr[nextinst],0, 230)
  fill(255,0,0)
  //turtle('LLLLLLLLLDDDDDDDDD')
  
}

function draw() {
  //nextinst = floor(random(instr.length))
  if (nextinst >= instr.length){ // testing if you have finished the list 
  	nextinst=0;
  	
  }
  //call generator function
  translate(50,50)
  myturtle.next();
  
  
  if (myturtle.next().done){ // seeing an instruction it is finished in generator fun
    background(0);  // reset for next instruction
    showlatt();
    nextinst = floor(random(instr.length))
    fill(0,255,0)
    text("path: "+nextinst+" "+instr[nextinst],0, 230)

    fill(random(255),random(255),random(255))
    myturtle = turtle();
    //nextinst++

  }
}



function showlatt(){
	stroke(0,255,0);
	for(let j =0; j<rowcol*sz; j+=sz){
		for (let i = 0; i <rowcol*sz; i+=sz){
			noFill();
			rect(i,j,sz,sz)
		}
	}
}



function* turtle(){

   ball.x =0;
   ball.y =0;
   stroke(0);
   //nextinst = floor(random(instr.length))


   rect(ball.x,ball.y,sz,sz);
   //text("path: "+nextinst+" "+instr[nextinst],0, 230)

   for (let i = 0; i < instr[nextinst].length; i++) {
    let current = instr[nextinst].charAt(i); // get char in sentence

    switch (current) {
     
        
       case "R":
       	ball.x+=sz;
       	rect(ball.x,ball.y,sz,sz);
        //yield
        break;

        case "D":
        ball.y+=sz;
        rect(ball.x,ball.y,sz,sz);
        //yield
        break;

      }
    yield;
    } 

}




/// code from
let findPermutations = (string) => {
  if (!string || typeof string !== "string"){
    return "Please enter a string"
  }

  if (!!string.length && string.length < 2 ){
    return string
  }

  let permutationsArray = [] 
   
  for (let i = 0; i < string.length; i++){
    let char = string[i]

    if (string.indexOf(char) != i)
    continue

    let remainder = string.slice(0, i) + string.slice(i + 1, string.length)

    for (let permutation of findPermutations(remainder)){
      permutationsArray.push(char + permutation) }
  }
  return permutationsArray
}
