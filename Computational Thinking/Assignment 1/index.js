
//the duets that the tasks wants to get scheduled
const duets=
[
    "A B",
    "E D",
    "A E",
    "B C",
    "D A",
    "F B",
    "C E",
    "B D",
    "D F",
    "F E",
]

//all possible permutations of the duets will be stored in here
const results=[];

//generates those possible permutations
generate(10,duets);

//filters the permutations to the possible solutions
const filtered=results.filter((result)=>checkDancers(result));

//prints the solutions in a convinient manner
filtered.forEach((res)=>console.log(
    res[0]+"->"+
    res[1]+"->"+
    res[2]+"->"+
    res[3]+"->"+
    res[4]+"->"+
    res[5]+"->"+
    res[6]+"->"+
    res[7]+"->"+
    res[8]+"->"+
    res[9]
    ));

//prints the number of possible solutions
console.log(filtered.length,results.length)


//checks every possible permutation if its a possible solution
function checkDancers(duets){

    //goes through the duets
    for(let k=1;k<duets.length;k++){
        const curDuet=duets[k];
        const lastDuet=duets[k-1];

        const curDancers=curDuet.split(" ");
        const lastDancers=lastDuet.split(" ");

        const lastAndCur=[...curDancers,...lastDancers];

        let stats=[
            {dancer:"A",amount:countInArray(lastAndCur,"A")},
            {dancer:"B",amount:countInArray(lastAndCur,"B")},
            {dancer:"C",amount:countInArray(lastAndCur,"C")},
            {dancer:"D",amount:countInArray(lastAndCur,"D")},
            {dancer:"E",amount:countInArray(lastAndCur,"E")},
            {dancer:"F",amount:countInArray(lastAndCur,"F")},
        ]

        //and checks wether we have two in a row (a requirement)
        if(!statsContainsAmountTimes(stats,2)){
            return false;
        }

        //then if we are not on the last rehearsal
        if(k===duets.length-1){
            return true;
        }
        const nextDuet=duets[k+1];
        const nextDancers=nextDuet.split(" ");

        const lastCurNext=[...curDancers,...lastDancers,...nextDancers];
        stats=[
            {dancer:"A",amount:countInArray(lastCurNext,"A")},
            {dancer:"B",amount:countInArray(lastCurNext,"B")},
            {dancer:"C",amount:countInArray(lastCurNext,"C")},
            {dancer:"D",amount:countInArray(lastCurNext,"D")},
            {dancer:"E",amount:countInArray(lastCurNext,"E")},
            {dancer:"F",amount:countInArray(lastCurNext,"F")},
        ]

        //we check whether a dancer hasn't danced 3 times in a row (also a requirement)
        if(statsContainsAmountTimes(stats,3)){
            return false;
        }

    }

    return true;
}

//returns how often what is in the given array
//used to check how many times a dancer has danced in the last 2/3 rehearsals
function countInArray(array, what) {
    return array.filter(item => item == what).length;
}

function statsContainsAmountTimes(stats,times){
    
    for(let s=0;s<stats.length;s++){
        if(stats[s].amount===times){
            return true;
        }
    }

    return false;
}

//generates all possible permutations using heaps algorithm
//I wrote this code based on the pseudo code of this article
//https://en.wikipedia.org/wiki/Heap%27s_algorithm#:~:text=Heap's%20algorithm%20generates%20all%20possible,2%20elements%20are%20not%20disturbed.
function generate(k,input){
    if(k===1){
        results.push([...input]);
    }
    else{
        generate(k - 1, input)

        for(let i=0;i<k-1;i++){
            if(k%2===0){
                input=swap(input,i,k-1)
            }
            else{
                input=swap(input,0,k-1)
            }
            generate(k-1,input)
        }
        
    }

}

//used by heaps algorithm
//swaps A with B in array
function swap(array, indexA, indexB) {
    var temp = array[indexA];
    array[indexA] = array[indexB];
    array[indexB] = temp;

    return array;
  };