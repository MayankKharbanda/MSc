var canvas = document.getElementsByTagName('canvas')[0];
var context = canvas.getContext("2d");		//to draw 2d drawings on canvas
var canvas_width = 400;						//dimentions of canvas
var canvas_height = 400;
var rows = 25;								//blockes alloted in each row and column
var cols = 25;
var blocks_width = Math.floor(canvas_width / cols);		//size of each block partitioned
var blocks_height = Math.floor(canvas_height / rows);
var game_over = false;
r = Math.floor(Math.random()*255);
g = Math.floor(Math.random()*255);
b = Math.floor(Math.random()*255);
r1=r;
g1=g;
b1=b;
// size of grid nxn
var size = rows;
  
// initialize grid
var game_area = grid(size);
  
// starting values 
var start_x = Math.floor(rows/2);
var start_y = Math.floor(cols/2);

// get the starting point of the item (apple)  
do {
  var food_x = Math.floor(Math.random() * size);
  var food_y = Math.floor(Math.random() * size);
} while (game_area[food_y][food_x].block == true)


// array for where the elements of the snake will be
var snake = new Array();
snake.push(game_area[start_y][start_x]);
game_area[start_y][start_x].block = true;

function Node(x, y) {
    this.block = false;
    this.x = x;  
    this.y = y;
    this.parent = null;
    this.g_value = -1; // score of getting from start to this node
    this.f_value = -1; // score of g_value plus hueristic value
    this.h_value = function (x_final, y_final) {
        return Math.floor(Math.abs(x_final - this.x) + Math.abs(y_final - this.y));
    };
}

// create 2D grid of of nxn where n = size
function grid(size) {
  
  // create array 
  var grid = new Array(size);
  for (var i = 0; i < size; i++) {
    grid[i] = new Array(size);
  }
  
  // associate each element with a node object
  for (var i = 0; i < size; i++) {
    for (var j = 0; j < size; j++) {
      if(grid[i][j] != "-") {
        grid[i][j] = new Node(j, i);
      }
    }
  }
  
  return grid;
}

// used to sort open set according to f_value values 
function f_valueSort(a,b) {
  if (a.f_value < b.f_value)
    return -1;
  if (a.f_value > b.f_value)
    return 1;
  return 0;
}

// checks to see if the current_node should be looked at
function bound_check(current_node, i, j) {
    // out of bounds
    if (((current_node.x + j) < 0) || ((current_node.x + j) > size - 1) || ((current_node.y + i) < 0) || ((current_node.y + i) > size - 1)) {
        return false;
    }

    // check to see if block is within the grid
    if ((game_area[current_node.y + i][current_node.x + j].block)) {
        return false;
    }

    // skip the current node
    if ((current_node.y + i == current_node.y && current_node.x + j == current_node.x)
        || ((i == -1) && (j == -1)) || ((i == -1) && (j == 1))
        || ((i == 1) && (j == -1)) || ((i == 1) && (j == 1))) {
        return false;
    }

    // if it passed all possible checks
    return true;
}


function A_Star() {
  
  // ending values 
  var end_x = food_x;
  var end_y = food_y;
  
  // set of nodes that have already been looked at
  var closedSet = [];
  
  // set of nodes that are known but not looked at 
  var openSet = [];

  // add the starting element to the open set
  openSet.push(game_area[start_y][start_x]);
  game_area[start_y][start_x].g_value = 0;
  game_area[start_y][start_x].f_value = game_area[start_y][start_x].h_value(end_x, end_y); // just the heuristic

  // while open set is not empty
  while (openSet.length > 0) {
    openSet.sort(f_valueSort);
    var current_node = openSet[0];
    
    if ((current_node.x == end_x) && (current_node.y == end_y)) {
      return reconstruct_path(game_area, current_node, start_x, start_y); // return path
    }
    
    // remove current node from open set
    var index = openSet.indexOf(current_node);
    openSet.splice(index, 1);
    
    closedSet.push(current_node);
    
    // looking at all of the node's neighbours
    for (var i = -1; i < 2; i++) {
      for (var j = -1; j < 2; j++) {

        if (!bound_check(current_node, i, j)) {
            continue;
        }

        var neighbour = game_area[current_node.y + i][current_node.x + j];
        
        // if node is within the closed set, it has already
        // been looked at - therefore skip it
        if (closedSet.indexOf(neighbour) != -1) {
          continue;
        }
        
        // set tentative score to g_value plus distance from current to neighbour
        // in this case, the weight is equal to 1 everywhere
        var tScore = neighbour.g_value + 1;
        
        // if neighbour is not in open set, add it
        if (openSet.indexOf(neighbour) == -1) {
          openSet.push(neighbour);
        }
        
        // this is a better path so set node's new values
        neighbour.parent = current_node;
        neighbour.g_value = tScore;
        neighbour.f_value = neighbour.g_value + neighbour.h_value(end_x, end_y);
        
      }
    }
  }
  
  // the node was not found or could not be reached
  return false;
  
}

function reconstruct_path(game_area, current, start_x, start_y) {
    var current_node = current;
    var totalPath = [current];
    
    // go through the parents to find how the route
    while (current_node.parent != null) {
      totalPath.push(current_node.parent);
      current_node = current_node.parent;
    }
    
    return totalPath;
}

// draws the board and the moving shape
function draw() {
    if (!game_over) {
        context.fillStyle = 'white';
		context.strokeStyle = 'black';
		
		context.fillRect(0, 0, canvas_width, canvas_height);
        context.strokeRect(0, 0, canvas_width, canvas_height);
        context.fillStyle = "rgb("+r+","+g+","+b+")";
		context.fillRect(blocks_width * food_x  , blocks_height * food_y, blocks_width , blocks_height);
		for(i=0; i<snake.length;i++){
			context.fillStyle = 'rgba('+r1+','+ g1 +','+ b1+', '+(1 - 0.7 * (i / snake.length))+')';
			context.fillRect(blocks_width * snake[i].x  , blocks_height * snake[i].y, blocks_width , blocks_height);
		}
    }
}

// get the next node for the snake to move
function getNextMove(end_x, end_y) {
    var nextLoc;
    var lowestf_value = -1;
    var lowestf_valueNode = null;
    for (var i = -1; i < 2; i++) {
        for (var j = -1; j < 2; j++) {

            if (!bound_check(snake[0], i, j)) {
                continue;
            }

            var neighbour = game_area[snake[0].y + i][snake[0].x + j];

            // pathScore = f_value + pathLength
            var pathScore = neighbour.g_value + neighbour.h_value(end_x, end_y) + pathLength(neighbour) + 1;

            // find the largest pathScore
            if (pathScore > lowestf_value) {
                lowestf_value = pathScore;
                lowestf_valueNode = neighbour;
            }
        }
    }

    return lowestf_valueNode;
}

// determine how many spaces are available to move given the current_node
function pathLength(current_node) {

    var currNode = current_node;
    var numOfNodes = 0;

    var longestPathArray = new Array();

    for (var i = -1; i < 2; i++) {
        for (var j = -1; j < 2; j++) {
        
            if (!bound_check(currNode, i, j)) {
                continue;
            }

            currNode = game_area[currNode.y + i][currNode.x + j];

            // increment the number of nodes and reset the check to looking at the top node
            numOfNodes++;
            i = -1;
            j = -1;

            longestPathArray.push(currNode);
            
            // check if no where else to go
            if ((!((currNode.x + 1) >= 0 && (currNode.x + 1) < size) || game_area[currNode.y][currNode.x + 1] == undefined || game_area[currNode.y][currNode.x + 1].block)
                && (!((currNode.x - 1) >= 0 && (currNode.x - 1) < size) || game_area[currNode.y][currNode.x - 1] == undefined || game_area[currNode.y][currNode.x - 1].block)
                && (!((currNode.y + 1) >= 0 && (currNode.y + 1) < size) || game_area[currNode.y + 1][currNode.x] == undefined || game_area[currNode.y + 1][currNode.x].block)
                && (!((currNode.y - 1) >= 0 && (currNode.y - 1) < size) || game_area[currNode.y - 1][currNode.x] == undefined || game_area[currNode.y - 1][currNode.x].block)) {

                // house keeping - reset blocks to false
                for (var i = 0; i < longestPathArray.length - 1; i++) {
                    longestPathArray[i].block = false;
                }

                return numOfNodes;
            }
            currNode.block = true;
        }
    }
}


function tick() {

    // keep track of where the trail is
    var tail;

    if (!game_over) {

        var path = A_Star();

        // clear the grid to perform the next set of calculations
        for (var j = 0; j < path.length - 1; j++) {
            path[j].parent = null;
            path[j].g_value = -1;
            path[j].f_value = -1;
        }

        for (var i = 0; i < game_area.length; i++) {
            for (var j = 0; j < game_area.length; j++) {
				game_area[i][j].parent = null;
                game_area[i][j].g_value = -1;
                game_area[i][j].f_value = -1;

            }
        }

        // if there is a path using A* to the item, go to the first node
        if (path) {
            var nextLoc = path[path.length - 2];
        } else { // otherwise, attempt to find the next best movement
            var nextNode = getNextMove(food_x, food_y);
            if (nextNode == null) {
                game_over = true;
                document.getElementById('gameover').innerHTML = "Game Over";
                return;
            } else {
                nextLoc = nextNode;
            }
        }

        // set next location
        snake.unshift(nextLoc) 
        nextLoc.block = true;
        start_x = nextLoc.x;
        start_y = nextLoc.y;

        // if not at the item, pop the tail
        if (!((nextLoc.x == food_x) && (nextLoc.y == food_y))) {
            tail = snake.pop();
            tail.block = false;
            tail.g_value = -1;
            tail.f_value = -1;
        } else { // if at the item, set a new item location
				r1=r;
				g1=g;
				b1=b;
				r = Math.floor(Math.random()*255);
				g = Math.floor(Math.random()*255);
				b = Math.floor(Math.random()*255);
			do {
                food_x = Math.floor(Math.random() * rows);
                food_y = Math.floor(Math.random() * rows);
            } while (game_area[food_y][food_x].block == true)
        }
    }
}


function startGame() {

    draw();

    setInterval( tick, 50 );
    setInterval( draw, 50 );

}

startGame();
