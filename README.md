# hotelManagement-python
My task was to read CSV file and compute the result asked by the user. The CSV file contains the record of cost and ratings of Hotels in Karnataka/ Tamilnadu/ Maharashtra.
My script should ask for the state, column to perform the opearation on and operations(cheapest,average,highest).

User Inputs <br>
1. State: It can be either one of Karnataka/ Tamilnadu/ Maharashtra which will give result for the corresponding state or India can also be an input which will perform the
   operation on all the states.<br>
2. Cost or Ratings: cost/ratings <br>
3. Operations cheapest/highest/average<br>

Sample 1<br>

What is the state: Karnataka.<br>
Cost or Ratings: cost.<br>
Operations: highest.<br>
Output: Hotel with Highest price in Karnataka is <hotel_code> with <cost_price>.<br>

Sample 2<br>
What is the state: India.<br>
Cost or ratings: rating.<br>
Operation: highest.<br>
Output: Hotel with highest ratings in Karnataka is <hotel_code> with <_rating>.<br>

Sample 3<br>
What is the state: Maharashtra.<br>
Cost or ratings: ratings.<br>
Operation: average.<br>
<!--on choosing average it has to return only the cost or ratings based on which state user had input.--!>
Output: Average ratings of Hotel in Maharashtra is <_rating>.
