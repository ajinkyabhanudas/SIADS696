# DEVELOPER NOTES
- Make sure to push into the `dev` branch only.
- `git checkout dev` (will switch your active branch to be dev locally)
- Before pushing your code with the downloaded data, make sure to do a `git pull` on the `dev branch` (this will download the latest changes locally for you and avoid merge conflicts)
- `git commit -m "<a few words on what is pushed>"`
- `git add .` adds all in all the changes
- `git push` to push the code into the `dev` branch repository

## How to downlaod the data?
- Open a console/terminal window and navigate to the `SIADS696` directory
- run `export API_KEY=<PUT_YOUR_API_KEY_HERE>`
- run `make get-data`
- Navigate to the `main.py` python script and comment out the channels you've successfully extracted data from to avoid a duplicate download.


# SIADS696
## Youtube Video Title Analysis and Views Prediction
<i>Ajinkya Bhanudas Dessai, Chauncey Raggie, Poom Khorchitmate</i>

### Project Overview
The goal of the project is to provide Youtube content creators with a way to gauge how effective a video title will be and to provide insight on which titles work best. Video titles are one of the main factors that determine whether people decide to click on a video or not. Coming up with a ‘formula’ for creating effective video titles would be advantageous to content creators. Phase I Our goal is to automate this process by first using supervised learning to determine if there is a relationship between the structure of a title and the number of views. Phase II we can provide the users with alternative title/word suggestions based on preferred topics.
### Unsupervised learning
#### Learning Approaches and Feature Representations
The goal for our unsupervised learning is to extract an underlying representation and evaluate the extent to which the meaning for each title can be used as a feature in the prediction. We will need to represent the video titles with an appropriate underlying representation using approaches such as a vector of word counts or weights, as well as extracting n-grams of text to help with the sparse data matrix using SVD.
K-means clustering (to help us discover underlying representation clusters)
tSNE, PCA(since the resulting vector projections and the resulting hyperspace are more meaningful).
#### Evaluation and Visualization
- Evaluation:
 The  best number of clusters, we will use the elbow method and silhouette score. 
- Visualization:
Once we get the K-means clustering we can evaluate the quality of the cluster once again using silhouette score. We then use t-SNE/PCA to visualize the clustering representations in the video’s titles.
Elbow plot for cluster choice, scree plot to choose the optimal number of PCA components.
### Supervised Learning
#### Learning Approaches and Feature Representations
Based on our engineered feature set, we will apply supervised learning methods to help predict the number of views. As for the models option we will work through the models based on complexity to better understand the challenges and utilities of each approach.
- Baseline model 1: Linear Regression. It’s great for underlying representations that are linear, simple and are interpretable.
- Baseline model 2: Tree-based Regressors: Interpretable, might be a better fit if the problem is non-linear.
- Experimental models:
  - KNN-regression (lazy learner, but the ability to handle non-linear data could show promise)
  - SVM based regression (if the engineered data has a very large feature set)
  - Basic Neural Networks (hypothesizing that remembering long range dependencies within the text won’t help improve the predictions)
#### Evaluation and Visualization
- Evaluation:
MSE/RMSE/MAE for model evaluation.
R-squared for the quality of fit.
LIME to help with interpretability in case we see a considerable performance improvement with  black box models.
- Visualization:
Word clouds.
Line charts, Bar charts for word density and spread-based analysis.
