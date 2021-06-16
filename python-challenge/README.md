# python-challenge

* Inside of each folder that I created:

  * A `main.py`. This is the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files used.
  * An "analysis" folder that contains your text file that has the results from my analysis.

## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, I created a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`.
* I created a Python script that analyzes the records to calculate each of the following:

  - [X] The total number of months included in the dataset
  - [X] The net total amount of "Profit/Losses" over the entire period
  - [X] The average of the changes in "Profit/Losses" over the entire period
  - [X] The greatest increase in profits (date and amount) over the entire period
  - [X] The greatest decrease in losses (date and amount) over the entire period
* Analysis looks similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

- [X] In addition, my final script both print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* A set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. I created a Python script that analyzes the votes and calculates each of the following:

  - [X] The total number of votes cast
  - [X] Complete list of candidates who received votes
  - [X] The percentage of votes each candidate won
  - [X] The total number of votes each candidate won
  - [X] The winner of the election based on popular vote.
* As an example, my analysis look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

- [X] In addition, my final script both print the analysis to the terminal and export a text file with the results.
