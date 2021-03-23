<a align="center" href = "https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/Recurrent_Neural_Networks_Case_Study.pdf">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/Paper-Front-Page.png?raw=true"
  width="1000" height="450">
</a>
In this case stugy we use Deep Learning, Recurrent Neural Networks with Long Short-Term Memory(LSTM) layers to predict the price of the Google stock. LSTM is more sophisticated version of RNN which addresses the Vanishing Gradient Problem that RNNs often suffer from. This project is based on the past Google stock prices of the last 5 years corresponding the time period of 2016-2020 that is used to train the RNN model and then use it to predict the upward and downward trends in the stock price of Google on January 2021.
<br>
This <a href = "https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/Recurrent_Neural_Networks_Case_Study.pdf"> Case Study Paper</a> and <a href = "https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/Recurrent_Neural_Network_Case_Study.py">Python Code</a> include:

  - Recurrent Neural Networks(RNNs)
  - RNN Optimization Process 
  - Vanishing Gradient Descent
  - Long Short-Term Memories (LSTMs)
  - GRU
  - Data Preproocessing 
  - Training/Testing/Evaluation
  - Results
<br>

# Data: Google Stock Price Data 
We have used <a href = "https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/tree/main/data">Google stock price data</a>, publicly available and downloaded from Yahoo Finance. For training the model we have used stock prices for the period of 2016-2020 and used it to predict stock prices for the January of 2021. 
<br><br>
You can download the <a href = "https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/data/Google_Stock_Price_Trainset.csv">Training Data here</a><br>
You can download the <a href = "https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/data/Google_Stock_Price_Testset.csv">Test Data here</a><br><br>
Google Stock Price Development Graph (Training Data)
<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/Google Stock Price Development.png?raw=true"
  width="600" height="300">
</p>
<br>
<br>

## Financial Data Preprocessing

<br>
In order to prepare the data to train and test RNN model we have performed certain data preprocessing steps using Tensorflow, Keras, Pandas and Scikit-Learn libraries. Detailed info about data preprocessing can be found in <a href = "https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/Recurrent_Neural_Networks_Case_Study.pdf"> Case Study Paper</a>
<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/data/Data transformation.png?raw=true"
  width="450" height="300">
</p>
<br>

## Recurrent Neural Networks
<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/methods/RNN's.png?raw=true"
  width="400" height="200">
</p>
<br>

<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/methods/hiddenstate_road.png?raw=true"
  width="300" height="200">
</p>
<br>


## GRU and LSTM for Vanishing Gradient Problem in RNNs
<br>
<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/methods/LSTM.png?raw=true"
  width="450" height="300">
</p>
<br>

<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/methods/GRU.png?raw=true"
  width="400" height="350">
</p>
<br>
<br>

## Long Short-Term Memory (LSTMs)
<br>
<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/methods/LSTM code.png?raw=true"
  width="600" height="430">
</p>
<br>

## Activation Functions (Sigmoid and Hyperbolic Tangent)
<br>
<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/methods/Hyperbolic_Tangent_Activation_Function.png?raw=true"
  width="270" height="250">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/methods/Sigmoid_Activation_Function.png?raw=true"
  width="280" height="250">
</p>
<br>

## Google Stock Price Prediction (Real Prices vs Predicted Prices)
<br>
<p align="left">
  <img src="https://github.com/TatevKaren/recurrent-neural-network-stock-price-predicition-case-study/blob/main/Prediction_Results.png?raw=true"
  width="600" height="400">
</p>
<br>




