/**
 * @param {number[][]} customers
 * @return {number}
 */
var averageWaitingTime = function(customers) {
    let total_wait = 0;
    let curr = 0;
    for(let i=0; i<customers.length; i++){
        let arrival = customers[i][0];
        let service = customers[i][1];
        if(curr < arrival) curr = arrival;
        let wait = curr - arrival + service;
        total_wait += wait;
        curr += service;
    }
    let avg_wait = total_wait / customers.length;
    return avg_wait;
};