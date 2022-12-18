'use strict';


var board = [0,0,0,0,0,0,0,0,0];
var next = 1; // 1 for X, -1 for O
var mode =  'pvb'; // mode 

var winning_conditions = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]];


function step(pos){
    if (board[pos]!=0){
        return -1;
    }
    // update button
    UpdateIcon(pos,next);
    // update board
    board[pos] = next;
    next = -next;

}

function randomstep(){

    var selected = [];
    var i;
    var selected_length = 0;
    for(i=0;i<9;i++){
        if(board[i]==0){
            selected.push(i);
            selected_length += 1;
        }
    }
    if(selected_length==0){
        return 0;
    }
    var random_idx = Math.floor(Math.random()*selected_length);
    
    step(selected[random_idx]);
}

function checkwinner(){


    var i;
    for(i = 0; i<8; i++){
        var pos_list = winning_conditions[i];

        if(board[pos_list[0]]==board[pos_list[1]] & board[pos_list[1]]==board[pos_list[2]] & board[pos_list[0]]!=0){
            return board[pos_list[0]]; // 1 for X, -1 for O
        }
    }

    var remain_slots = 0;
    for(i = 0; i<9; i++){
        if(board[i]==0){
            remain_slots += 1;
        }
    }
    if(remain_slots==0){
        return 2;
    }
    return 0;
}

function UpdateIcon(pos,icon_idx){

    console.assert(icon_idx==-1 | icon_idx==1);
    var button = document.getElementById("block_"+pos);
    if(icon_idx==-1){
        button.classList.toggle("iconize1");
    }
    else{
        button.classList.toggle("iconize2");
    }

    button.disabled=true;
}

function LockAll(){
    var i;
    for(i = 0; i<9; i++){
        var button = document.getElementById("block_"+i);
        button.disabled=true;
    }
}

function UnlockAll(){
    var i;
    for(i = 0; i<9; i++){
        var button = document.getElementById("block_"+i);
        button.disabled=false;
    }
}


function Restart(){
    var i;
    for(i = 0; i<9; i++){
        var button = document.getElementById("block_"+i);
        button.disabled=false;
        if(board[i]!=0){
            if(board[i]==1){
                //button.click()
                button.classList.toggle("iconize2");
            }
            else{
                //button.click()
                button.classList.toggle("iconize1");   
            }

            //button.classList.toggle("resetall");
        }
        board[i]=0;
    }
    next = 1;
    UpdateText(0,next);
}


function Onclicked(pos){
    var winner;
    step(pos);
    winner = checkwinner();
    UpdateText(winner,next);
    if(winner!=0){
        LockAll();
        return;
    }
    if(document.getElementById('gamemode').getAttribute("value")=="pvb"){
        randomstep();  
        winner = checkwinner();
        UpdateText(winner,next);
        if(winner!=0){
            LockAll();
        }
    }
}

function UpdateText(winner,next){
    if(winner==0){
        if(next==1){
            document.getElementById("status").innerHTML = "It's X turn";
        }
        else if(next==-1){
            document.getElementById("status").innerHTML = "It's O turn";
        }
    }
    else if(winner==2){
        document.getElementById("status").innerHTML = "Draw!";
    }
    else if(winner == 1){
        document.getElementById("status").innerHTML = "X wins!";
    }
    else if(winner == -1){
        document.getElementById("status").innerHTML = "O wins!";
    }
    
}