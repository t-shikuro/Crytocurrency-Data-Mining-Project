# CSPB-4502-Data-Mining-Project


## Group 2 Team Members
* Inderpal Dhillon
* James Beedle
* Lauren Deans
* Theo Shin

# Project Description
Looking at past cryptocurrency trends using 'DataJuicers cryptodatabase' to build a prediction modeler. The .csv file contains ticks for all tradable currecies (bitcoin, ethereum, litecoin, ripple) beginning 2018-08-15. There are 39 days of transaction data within the dataset.

We used multiple data analysis and machine learning techniques to analyze the dataset and search for correlations within the data. The analysis methods we used include:
* Multilinear Regression Analysis
* Decision Trees
* K-Nearest Neighbor
* Dickey-Fuller Statistical Test
* Random Forest Model
***

## Summary of Questions:
Questions we sought to answer include how a $1 increase in Bitcoin affects other cryptocurrencies (Bitcoin cash, Ethereum, Litecoin, and Ripple) as well as how to best set up a dataset for predictive modeling methods.

We determined that a $1 increase in Bitcoin will yield the following results:
Given a 1$ increase in bitcoin, on average the coins reacted as follows:
* BCH = - $0.0162
* ETH = - $0.0182
* LTC = + $0.0082
* XRP = - 2.394e-05

***

## Application of the Knowledge:
Looking at this at a high level, this model will attempt to tell us if the current market price of a coin is below what it is really worth in comparison to the other coins because of the fairly tight correlation of price movements, especially with LTC. If we assume what we have observed in the past is true for the future, we can trade based on this. In the event that we are correct we will make a ton of money, but if we are incorrect, we could amplify our losses.

Consider these fabricated trades as an example:
* 2018-08-15 18:55:02 BTC traded at 6519.39	  LTC traded at 57.82
* 2018-08-15 18:55:03 BTC traded at 6519.60	
* 2018-08-15 18:55:05 BTC traded at 6520.39 

The price of BTC went up by a dollar in a short span of 4 seconds. The last LTC trade executed was at the first second of the minute at 57.82. According to our algorithm, the value of LTC at 18:55:05 given the rise in BTC is 57.8282. Our goal now is to buy as many LTC coins in the open market for under 57.8282 as possible. During the inverse event when the price is dropping, our algorithm will attempt to sell coins it deems as overvalued. If our model turns out to be accurate, and we are fast enough. Over the long run, we will be able to keep these small differences between our predicted value of a coin and its market value as profit.
***

## Link to Video Demonstration

## Link to Final Project Paper
